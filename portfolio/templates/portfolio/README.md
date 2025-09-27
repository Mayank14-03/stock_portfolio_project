# Stock Portfolio Tracker

A Django web application to **track stock holdings, calculate returns, and manage portfolio performance**. This project allows users to add, update, and delete stock holdings, view current stock prices, and analyze their investment portfolio.

---

## Features

- Add, update, and delete stock holdings.
- Validate stock symbols automatically.
- Calculate profit/loss for each stock and total portfolio.
- Display current stock prices and portfolio performance.
- User-friendly dashboard to manage investments.
- Built using Django and Python.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Mayank14-03/stock_portfolio_project.git

2.Navigate to project folder

cd stock_portfolio_project


3.Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


4.Install dependencies

pip install -r requirements.txt


5.Apply migrations

python manage.py migrate


6.Run the development server

python manage.py runserver


7.Open your browser at: 
  http://127.0.0.1:8000/

Usage:

Add a stock to your portfolio using the “Add Holding” form.

Update or delete stocks from the dashboard.

View your current portfolio performance, including total returns and profit/loss.

⚠️ Note: Use valid stock symbols (e.g., Apple = AAPL). Invalid symbols will be rejected.


Technologies Used:

Python 3.x

Django 4.x

HTML, CSS, Bootstrap

yfinance (for fetching stock data)

Future Improvements

Add user authentication (login/register).

Support for multiple portfolios per user.

Interactive charts for portfolio performance.

Auto-suggestions for stock symbols.


Author:

Mayank Korde

GitHub: https://github.com/Mayank14-03

LinkedIn: https://www.linkedin.com/in/mayank-korde-386bb1317/


License:

This project is open-source and available under the MIT License.


---

⚡ Tip: After saving this as `README.md`, **commit and push** it to GitHub:  

```powershell
git add README.md
git commit -m "Add professional README.md"
git push

