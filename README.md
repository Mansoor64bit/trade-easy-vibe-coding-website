# 📈 TradeEasy – Financial Literacy Platform

## Overview

TradeEasy is a full-stack web application developed to promote financial literacy and introduce users to essential investment concepts through a simple and interactive learning platform.

The application provides educational modules covering different financial instruments while offering a secure user experience through authentication and database-backed functionality.

---

## Project Objectives

- Improve financial awareness among users
- Introduce core investment concepts
- Provide a structured learning experience
- Demonstrate full-stack web development skills

---

## Key Features

### User Authentication

- User registration
- Secure login functionality
- Session management

### Financial Learning Modules

Educational sections covering:

- Stocks
- Mutual Funds
- Gold Investments
- Futures and Options (F&O)

### Financial Literacy Assessment

- Interactive forms
- Knowledge tracking
- User responses stored in database

### Database Management

- SQLite database integration
- Dynamic data storage and retrieval
- Database initialization through Python scripts

### Responsive User Interface

- HTML5 templates
- CSS styling
- Jinja2 templating engine
- Mobile-friendly design

---

## Technology Stack

### Backend

- Python
- Flask
- Jinja2

### Frontend

- HTML5
- CSS

### Database

- SQLite

### Development Tools

- Virtual Environment (venv)
- pip

---

## Project Structure

```text
app.py              Main Flask application
init_db.py          Database initialization
templates/          HTML templates
static/             CSS and static assets
database/           SQLite database files
```

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/tradeeasy-financial-literacy-platform.git
```

### 2. Navigate to Project Directory

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

### 7. Access Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Skills Demonstrated

- Full Stack Development
- Python Programming
- Flask Framework
- Database Design
- Authentication Systems
- Frontend Development
- Backend Development
- Problem Solving

---

## Future Enhancements

- User dashboard
- Investment calculators
- Market data integration
- Financial quizzes
- Portfolio tracking tools

---

## Disclaimer

This project was developed for educational and portfolio purposes.
