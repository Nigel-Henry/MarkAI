import sqlite3

def init_db():
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS api_keys (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            api_key TEXT UNIQUE,
            key_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()