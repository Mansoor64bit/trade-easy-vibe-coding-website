# 📈 TradeEasy

## 📌 Project Overview
**TradeEasy** is a full-stack web application designed to simplify financial literacy and introduce users to core trading concepts. Built with Python and the Flask framework, the platform offers an intuitive, interactive environment where users can learn about different investment vehicles and track their financial knowledge.

## 🚀 Key Features
*   **User Authentication:** Secure registration and login functionality.
*   **Financial Modules:** Dedicated, easy-to-navigate interfaces for Stocks, Mutual Funds, Gold, and Futures & Options (F&O).
*   **Knowledge Tracking:** Integrated financial literacy forms to assess and improve user understanding of markets.
*   **Dynamic Data Management:** A robust SQLite database initialized and managed via custom Python scripts.
*   **Responsive UI:** Clean, accessible frontend templates built with HTML5, CSS, and Jinja2.

## 🛠️ Technology Stack
*   **Backend:** Python, Flask, Jinja2
*   **Database:** SQLite
*   **Frontend:** HTML5, CSS
*   **Environment Management:** pip, Virtualenv

## 💻 Local Setup Instructions
Follow these steps to run the TradeEasy application on your local machine:

1. **Clone the repository**
   git clone https://github.com/YourUsername/trade-easy-flask.git

2. **Navigate to the project directory**
   cd trade-easy-flask

3. **Create and activate a virtual environment**
   * Windows: `python -m venv venv` and then `venv\Scripts\activate`
   * Mac/Linux: `python3 -m venv venv` and then `source venv/bin/activate`

4. **Install required dependencies**
   pip install -r requirements.txt

5. **Initialize the database**
   python init_db.py

6. **Run the Flask application**
   python app.py

7. **View the app**
   Open your web browser and navigate to `http://127.0.0.1:5000`

---
*Developed as a comprehensive web development and financial literacy project.*
