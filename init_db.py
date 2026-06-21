import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'app.db')

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create users table (keep password simple for now — see README for next steps)
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Create contacts table for messages from contact form
c.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
# Note: financial literacy form tables removed per request.
# If you need to permanently delete existing tables from an existing
# database file, run appropriate DROP TABLE commands directly against
# the database (handled separately). This initializer will no longer
# create financial literacy-related tables.

conn.commit()
conn.close()
print('Initialized database at', DB_PATH)
