import sqlite3

def init_db():
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS knowledge 
                     (id INTEGER PRIMARY KEY, topic TEXT, content TEXT)''')
        conn.commit()

def insert_knowledge(topic, content):
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO knowledge (topic, content) VALUES (?, ?)', (topic, content))
        conn.commit()

def get_knowledge():
    with sqlite3.connect('knowledge.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM knowledge')
        return c.fetchall()

# Initialize the database
init_db()