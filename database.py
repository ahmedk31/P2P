import sqlite3

def setup_database():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, from_user TEXT, to_user TEXT, message TEXT, sent INTEGER DEFAULT 0, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_message(from_user, to_user, message):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (from_user, to_user, message) VALUES (?, ?, ?)", (from_user, to_user, message))
    conn.commit()
    conn.close()

def fetch_pending_messages(to_user):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT message FROM messages WHERE to_user = ? AND sent = 0", (to_user,))
    messages = c.fetchall()
    conn.close()
    return messages

def mark_messages_as_sent(to_user):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("UPDATE messages SET sent = 1 WHERE to_user = ?", (to_user,))
    conn.commit()
    conn.close()
