import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'app.db')

TABLES_TO_DROP = [
    'financial_literacy_forms',
    'financial_literacy_quiz_results',
    'financial_literacy'
]

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

for t in TABLES_TO_DROP:
    try:
        c.execute(f"DROP TABLE IF EXISTS {t}")
        print(f"Dropped table if existed: {t}")
    except Exception as e:
        print(f"Error dropping {t}: {e}")

conn.commit()
conn.close()
print('Done')
