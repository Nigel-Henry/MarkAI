import sqlite3

def init_db():
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                plan TEXT
            )
        ''')
        conn.commit()

def insert_subscription(user_id, plan):
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO subscriptions (user_id, plan)
            VALUES (?, ?)
        ''', (user_id, plan))
        conn.commit()

def get_subscriptions():
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM subscriptions')
        return c.fetchall()

# Initialize the database
init_db()