# 📈 TradeEasy – Financial Literacy Web Application

## Overview

TradeEasy is a web application developed using Python and Flask to help users learn the fundamentals of investing and financial markets.

The platform provides educational modules covering different investment options such as Stocks, Mutual Funds, Gold, and Futures & Options (F&O). Users can also complete a financial literacy form to assess their understanding of financial concepts.

This project was developed as part of a web development learning project and demonstrates full-stack application development using Python, Flask, SQLite, HTML, and CSS.

---

## Features

### User Authentication

- User Registration
- User Login
- Session Management

### Financial Learning Modules

The application contains dedicated sections for:

- Stocks
- Mutual Funds
- Gold Investments
- Futures & Options (F&O)

### Financial Literacy Assessment

- Interactive financial literacy form
- User response collection
- Database storage

### Contact Page

- User contact interface
- Basic inquiry submission

### Database Integration

- SQLite database backend
- User information storage
- Financial literacy form records

---

## Technology Stack

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS

### Database

- SQLite

---

## Project Files

```text
app.py                     Main Flask Application
init_db.py                 Database Initialization Script
drop_financial_tables.py   Database Maintenance Script

index.html                 Homepage
login.html                 Login Page
contact.html               Contact Page

stocks.html                Stocks Module
mutualfunds.html           Mutual Funds Module
gold.html                  Gold Investment Module
fo.html                    Futures & Options Module

literacyform.html          Financial Literacy Form

app.db                     SQLite Database
requirements.txt           Project Dependencies
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/tradeeasy-financial-literacy-platform.git
```

### 2. Navigate to Project Folder

```bash
cd tradeeasy-financial-literacy-platform
```

### 3. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Initialize Database

```bash
python init_db.py
```

### 6. Run Application

```bash
python app.py
```

### 7. Open Application

Visit:

```text
http://127.0.0.1:5000
```

---

## Skills Demonstrated

- Python Programming
- Flask Web Development
- Database Management
- SQLite Integration
- User Authentication
- HTML & CSS
- Backend Development
- Problem Solving

---

## Screenshots

Add screenshots of:

- Home Page
- Login Page
- Stocks Module
- Mutual Funds Module
- Gold Module
- F&O Module
- Financial Literacy Form

inside a `/screenshots` folder.

---

## Future Improvements

- User Dashboard
- Investment Calculators
- Portfolio Tracking
- Market Data Integration
- Better UI Design
- Admin Panel

---

## Disclaimer

This project was developed for educational and portfolio purposes. The information provided within the application is intended for learning and awareness and should not be considered financial advice.
