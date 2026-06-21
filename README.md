# Flask + SQLite backend for TradeEasy Vibe

This project adds a minimal Flask backend that serves your existing HTML files (from the project root) and provides simple API endpoints backed by SQLite.

Files added:
- `app.py` — Flask application. Serves your existing HTML pages and exposes API endpoints:
  - `POST /api/contact` — accepts form fields `name`, `email`, `message` (saves to `contacts` table)
  - `POST /api/register` — accepts `username`, `password` (adds to `users` table)
  - `POST /api/login` — accepts `username`, `password` (simple auth check)
- `init_db.py` — creates `app.db` and the tables `users` and `contacts`
- `requirements.txt` — Python dependencies
- `.gitignore` — ignore virtualenv and DB

How to run (PowerShell):

1) Create a virtual environment and activate it

```powershell
python -m venv .\venv
.\venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
pip install -r requirements.txt
```

3) Initialize the database

```powershell
python init_db.py
```

4) Run the app

```powershell
python app.py
```

The Flask app runs in debug mode on http://127.0.0.1:5000/ and will serve your existing HTML files (e.g., `index.html`, `login.html`, `contact.html`, `stocks.html`) from the project root. Use your forms to POST to the API endpoints above.

Security & next steps (recommended):
- Hash passwords with `bcrypt` or `werkzeug.security.generate_password_hash` before saving.
- Add sessions or JWT for auth instead of the current stateless check.
- Add server-side input validation and CSRF protection for forms.
- Move HTML into a `templates/` folder and use `render_template` for more advanced pages.
- Add simple unit tests for the API.
