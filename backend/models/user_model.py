import sqlite3

class User:
    def __init__(self, id, username, password, role, twofa_secret, biometric_key=None, points=0):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.twofa_secret = twofa_secret
        self.biometric_key = biometric_key
        self.points = points

def get_db_connection():
    return sqlite3.connect('knowledge.db')

def init_db():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                role TEXT,
                twofa_secret TEXT,
                biometric_key TEXT,
                points INTEGER DEFAULT 0
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS rewards (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                reward_name TEXT,
                points_required INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

def add_user(username, password, role, twofa_secret, biometric_key=None):
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO users (username, password, role, twofa_secret, biometric_key)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, password, role, twofa_secret, biometric_key))
        conn.commit()

def get_all_users():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        return c.fetchall()

def add_reward(user_id, reward_name, points_required):
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO rewards (user_id, reward_name, points_required)
            VALUES (?, ?, ?)
        ''', (user_id, reward_name, points_required))
        conn.commit()

def get_all_rewards():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM rewards')
        return c.fetchall()

# تهيئة قاعدة البيانات
init_db()
