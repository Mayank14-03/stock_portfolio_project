# 📊 Stock Portfolio Tracker

A Django web application to **track stock holdings, calculate returns, and manage portfolio performance**.  
Easily add, update, and delete stock holdings, view live stock prices, and analyze your investments.

---

## ✨ Features

- ➕ Add, ✏️ update, and ❌ delete stock holdings  
- 🔍 Validate stock symbols automatically  
- 📈 Calculate profit/loss for each stock and total portfolio  
- 💹 View current stock prices and portfolio performance  
- 🖥️ User-friendly dashboard to manage investments  
- ⚡ Built using Django, Python, and yfinance  

---

## 🚀 Demo (Screenshots)

| Dashboard | Add Holding Page |
|-----------|------------------|
| ![Dashboard Screenshot](screenshots/dashboard.png) | ![Add Stock Screenshot](screenshots/add_stock.png) |

*(Add your screenshots inside a `screenshots/` folder and update the image paths)*

---

## ⚙️ Installation

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


📌 Usage

Add a stock to your portfolio using the “Add Holding” form

Update or delete stocks directly from the dashboard

View your portfolio performance, profit/loss, and returns

⚠️ Use valid stock symbols (e.g., Apple = AAPL). Invalid symbols will be rejected


🛠️ Technologies Used

Python 3.x

Django 4.x

HTML, CSS, Bootstrap

yfinance (for fetching stock data)


🌟 Future Improvements

🔑 User authentication (login/register)

📊 Interactive charts for portfolio performance

🧾 Multiple portfolios per user

📝 Auto-suggestions for stock symbols


👨‍💻 Author

Mayank Korde

GitHub: https://github.com/Mayank14-03

LinkedIn: https://www.linkedin.com/in/mayank-korde-386bb1317/


📄 License

This project is open-source and available under the MIT License.


🏆 Badges

---

### ✅ What to Do Next:
1. Copy this into your `README.md`.  
2. Create a `screenshots/` folder in your project → add images of your dashboard, forms, etc.  
3. Commit & push:  
   ```powershell
   git add README.md
   git commit -m "Update polished README with badges and screenshots"
   git push

