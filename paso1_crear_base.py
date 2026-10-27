import sqlite3

conn = sqlite3.connect("tienda.db") # It creates
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
"""
)

new_users = [
    ("Ana Lopez", "ana@email.com"),
    ("Maria Perez", "maria@email.com"),
    ("Juan Torres", "juan@email.com"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
    new_users,
)
conn.commit()

cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print(user)

conn.close()