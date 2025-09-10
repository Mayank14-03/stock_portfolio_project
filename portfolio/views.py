from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Holding
from .forms import HoldingForm

import yfinance as yf
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend to prevent server crashes
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd


# ----------------------------
# Custom Login View
# ----------------------------
class CustomLoginView(LoginView):
    template_name = 'portfolio/login.html'


# ----------------------------
# Register View
# ----------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/register.html', {'form': form})


# ----------------------------
# Dashboard View
# ----------------------------
@login_required
def dashboard(request):
    holdings = Holding.objects.filter(user=request.user)
    total_value = 0
    total_profit = 0

    # Calculate portfolio values
    for h in holdings:
        try:
            data = yf.Ticker(h.stock_symbol)
            current_price = data.info.get('regularMarketPrice', 0)
        except Exception:
            current_price = 0  # fallback if Yahoo API fails

        h.current_price = current_price
        h.profit_loss = (current_price - h.purchase_price) * h.quantity
        h.is_profit = h.profit_loss >= 0
        total_value += current_price * h.quantity
        total_profit += h.profit_loss

    profit_positive = total_profit >= 0

    # Generate Pie Chart
    chart = None
    if holdings:
        labels = [h.stock_symbol for h in holdings]
        sizes = [h.current_price * h.quantity for h in holdings]

        fig, ax = plt.subplots(figsize=(5, 5))
        theme = "dark_background" if request.COOKIES.get("theme") == "dark" else "default"
        plt.style.use(theme)

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')

        buf = io.BytesIO()
        plt.savefig(buf, format='png', transparent=True)
        buf.seek(0)
        chart = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()

    return render(request, 'portfolio/dashboard.html', {
        'holdings': holdings,
        'total_value': total_value,
        'total_profit': total_profit,
        'profit_positive': profit_positive,
        'chart': chart
    })


# ----------------------------
# Add Holding
# ----------------------------
@login_required
def add_holding(request):
    if request.method == 'POST':
        form = HoldingForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['stock_symbol'].upper()

            try:
                data = yf.Ticker(symbol)
                current_price = data.info.get('regularMarketPrice')
            except Exception as e:
                messages.error(request, f"Failed to fetch stock data: {e}")
                return render(request, 'portfolio/add_holding.html', {'form': form})

            if current_price is None:
                messages.error(request, f"'{symbol}' is not a valid stock symbol!")
                return render(request, 'portfolio/add_holding.html', {'form': form})

            # Save holding
            holding = form.save(commit=False)
            holding.user = request.user
            holding.stock_symbol = symbol
            if hasattr(holding, "current_price"):  # only if field exists in model
                holding.current_price = current_price
            holding.save()

            messages.success(request, f"Holding '{symbol}' added successfully!")
            return redirect('portfolio:dashboard')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = HoldingForm()

    return render(request, 'portfolio/add_holding.html', {'form': form})


# ----------------------------
# Edit Holding
# ----------------------------
@login_required
def edit_holding(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)

    if request.method == 'POST':
        form = HoldingForm(request.POST, instance=holding)
        if form.is_valid():
            symbol = form.cleaned_data['stock_symbol'].upper()
            try:
                data = yf.Ticker(symbol)
                if data.info.get('regularMarketPrice') is None:
                    messages.error(request, f"'{symbol}' is not a valid stock symbol!")
                    return render(request, 'portfolio/edit_holding.html', {'form': form, 'edit': True})
            except Exception:
                messages.error(request, f"Failed to fetch stock data for '{symbol}'.")
                return render(request, 'portfolio/edit_holding.html', {'form': form, 'edit': True})

            form.save()
            messages.success(request, f"Holding '{symbol}' updated successfully!")
            return redirect('portfolio:dashboard')
    else:
        form = HoldingForm(instance=holding)

    return render(request, 'portfolio/edit_holding.html', {'form': form, 'edit': True})


# ----------------------------
# Delete Holding
# ----------------------------
@login_required
def delete_holding(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)
    if request.method == 'POST':
        holding.delete()
        messages.success(request, f"Holding '{holding.stock_symbol}' deleted successfully!")
        return redirect('portfolio:dashboard')
    return render(request, 'portfolio/delete_holding.html', {'holding': holding})


# ----------------------------
# Export Excel
# ----------------------------
@login_required
def export_excel(request):
    holdings = Holding.objects.filter(user=request.user)
    data = []

    for h in holdings:
        try:
            current_price = yf.Ticker(h.stock_symbol).info.get('regularMarketPrice', 0)
        except Exception:
            current_price = 0
        profit_loss = (current_price - h.purchase_price) * h.quantity
        data.append({
            'Stock Symbol': h.stock_symbol,
            'Quantity': h.quantity,
            'Purchase Price': h.purchase_price,
            'Current Price': current_price,
            'Profit/Loss': profit_loss
        })

    df = pd.DataFrame(data)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=portfolio.xlsx'
    df.to_excel(response, index=False)
    return response


# ----------------------------
# Forgot Username
# ----------------------------
def forgot_username(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            send_mail(
                subject="Your Username",
                message=f"Hello, your username is: {user.username}",
                from_email="admin@yourapp.com",
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, "Your username has been sent to your email.")
        except User.DoesNotExist:
            messages.error(request, "No user found with this email.")
    return render(request, "portfolio/forgot_username.html")




