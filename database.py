import sqlite3

def get_db_connection():
    conn = sqlite3.connect('memos.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.executescript('''
    DROP TABLE IF EXISTS memos;
    CREATE TABLE memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        tags TEXT
    );
    ''')
    conn.close()
