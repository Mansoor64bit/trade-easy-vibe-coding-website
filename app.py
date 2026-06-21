from flask import Flask, g, request, jsonify, send_from_directory, session, redirect, url_for
import sqlite3
import os
import secrets

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'app.db')

app = Flask(__name__, static_folder=None)
app.secret_key = secrets.token_hex(16)  # Generate a secure secret key for sessions

# --- Database helpers ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Static HTML serving (serves the existing HTML files in the project root) ---
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')



# Generic file route for your HTML pages (e.g., /login.html, /contact.html, /stocks.html)
@app.route('/<path:filename>')
def serve_file(filename):
    # Basic safety: only allow files in the project root (you can expand this list)
    return send_from_directory(BASE_DIR, filename)

# --- API endpoints ---
@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not (name and email and message):
        return jsonify({'error': 'name, email, and message are required'}), 400
    db = get_db()
    cur = db.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    db.commit()
    return jsonify({'status': 'ok', 'id': cur.lastrowid}), 201

@app.route('/api/financial-literacy', methods=['POST'])
def api_financial_literacy():
    # Financial literacy form storage has been removed.
    # Previously this endpoint accepted form submissions and quiz results
    # and stored them in the local SQLite database. Those tables were
    # removed from the initializer. Return 410 Gone to indicate the
    # resource is no longer available.
    return jsonify({
        'error': 'Financial literacy form storage has been removed'
    }), 410

@app.route('/api/watchlist', methods=['GET', 'POST'])
def api_watchlist():
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    db = get_db()
    if request.method == 'POST':
        data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
        if not data.get('stock_symbol'):
            return jsonify({'error': 'stock_symbol is required'}), 400
        
        cur = db.execute('''
            INSERT INTO stock_watchlist 
            (user_id, stock_symbol, company_name, target_price, notes)
            VALUES (?, ?, ?, ?, ?)
        ''', (session['user_id'], data['stock_symbol'], data.get('company_name'),
              data.get('target_price'), data.get('notes')))
        db.commit()
        return jsonify({'status': 'ok', 'id': cur.lastrowid}), 201
    else:
        stocks = db.execute('SELECT * FROM stock_watchlist WHERE user_id = ?', 
                          (session['user_id'],)).fetchall()
        return jsonify([dict(s) for s in stocks])

@app.route('/api/mutual-funds', methods=['GET', 'POST'])
def api_mutual_funds():
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    db = get_db()
    if request.method == 'POST':
        data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
        required = ['fund_name', 'investment_amount', 'units', 'investment_type']
        if not all(data.get(f) for f in required):
            return jsonify({'error': 'Missing required fields'}), 400
        
        cur = db.execute('''
            INSERT INTO mutual_fund_investments 
            (user_id, fund_name, investment_amount, units, purchase_date, investment_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session['user_id'], data['fund_name'], data['investment_amount'],
              data['units'], data.get('purchase_date'), data['investment_type']))
        db.commit()
        return jsonify({'status': 'ok', 'id': cur.lastrowid}), 201
    else:
        funds = db.execute('SELECT * FROM mutual_fund_investments WHERE user_id = ?', 
                         (session['user_id'],)).fetchall()
        return jsonify([dict(f) for f in funds])

@app.route('/api/gold-investments', methods=['GET', 'POST'])
def api_gold():
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    db = get_db()
    if request.method == 'POST':
        data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
        required = ['investment_type', 'quantity', 'purchase_price']
        if not all(data.get(f) for f in required):
            return jsonify({'error': 'Missing required fields'}), 400
        
        cur = db.execute('''
            INSERT INTO gold_investments 
            (user_id, investment_type, quantity, purchase_price, purchase_date, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session['user_id'], data['investment_type'], data['quantity'],
              data['purchase_price'], data.get('purchase_date'), data.get('notes')))
        db.commit()
        return jsonify({'status': 'ok', 'id': cur.lastrowid}), 201
    else:
        investments = db.execute('SELECT * FROM gold_investments WHERE user_id = ?', 
                              (session['user_id'],)).fetchall()
        return jsonify([dict(i) for i in investments])

@app.route('/api/portfolio', methods=['GET'])
def api_portfolio():
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    db = get_db()
    portfolio = db.execute('''
        SELECT * FROM portfolio_summary 
        WHERE user_id = ? 
        ORDER BY last_updated DESC 
        LIMIT 1
    ''', (session['user_id'],)).fetchone()
    
    if portfolio:
        return jsonify(dict(portfolio))
    return jsonify({'error': 'No portfolio data found'}), 404

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
    username = data.get('username')
    password = data.get('password')
    if not (username and password):
        return jsonify({'error': 'username and password required'}), 400
    db = get_db()
    existing = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
    if existing:
        return jsonify({'error': 'user already exists'}), 409
    db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    db.commit()
    return jsonify({'status': 'ok'}), 201

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.form.to_dict() if request.form else (request.get_json(silent=True) or {})
    username = data.get('username')
    password = data.get('password')
    if not (username and password):
        return jsonify({'error': 'username and password required'}), 400
    db = get_db()
    user = db.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    if user:
        session['username'] = username  # Store username in session
        return jsonify({'status': 'ok', 'user_id': user['id'], 'username': username})
    return jsonify({'error': 'invalid credentials'}), 401

@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop('username', None)  # Remove username from session
    return jsonify({'status': 'ok'})

@app.route('/api/check-auth', methods=['GET'])
def api_check_auth():
    username = session.get('username')
    if username:
        return jsonify({'status': 'ok', 'username': username})
    return jsonify({'status': 'not_authenticated'}), 401

if __name__ == '__main__':
    # Development server
    app.run(debug=True)
