# Stock Portfolio Tracker Project

A Django-based web application to track your stock portfolio with real-time prices, portfolio charts, and Excel export. Fully mobile responsive and supports dark/light mode.

---

## Tech Stack
- **Python 3.x**  
- **Django 5.x**  
- **MySQL**  
- **yfinance** (for stock prices)  
- **Matplotlib** (for charts)  
- **HTML, CSS, JavaScript**

---

## Features
- Dashboard with portfolio summary  
- Add/Edit/Delete Holdings  
- Portfolio Trend Chart (Pie chart of holdings)  
- Profit/Loss color coding (Green for profit, Red for loss)  
- Export portfolio to Excel  
- Dark/Light mode toggle  
- Fully mobile responsive  
- Password reset functionality  
- Login/Register functionality  

---

## Screenshots

**Dashboard**  
![Dashboard](stock_portfolio/screenshots/dashboard.png)

**Add Holding**  
![Add Holding](stock_portfolio/screenshots/add_holding.png)

**Portfolio Chart**  
![Portfolio Chart](stock_portfolio/screenshots/chart.png)

**Login Page**  
![Login](stock_portfolio/screenshots/login.png)

---

## How to Run Locally

1. Clone the repository:

```bash
(https://github.com/Mayank14-03/stock_portfolio_tracker_project.git)
Go into the project folder:

bash
Copy code
cd stock_portfolio_tracker_project
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install requirements:

bash
Copy code
pip install -r requirements.txt
Configure MySQL database in settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open in browser at http://127.0.0.1:8000/

Notes
Screenshots folder: Create a folder named /stock_portfolio/screenshots/ in your repo and add the images there.

.gitignore: Make sure to exclude venv/, __pycache__/, .env, and other local files.

Repo name: If you want, rename your GitHub repository to match your project folder for consistency.

Author
Mayank Korde
GitHub | LinkedIn

