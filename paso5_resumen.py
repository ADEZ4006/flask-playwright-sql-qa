import sqlite3

conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

cursor.execute(
    """
    SELECT users.name, SUM(orders.price)
    FROM users
    JOIN orders ON users.id = orders.user_id
    GROUP BY users.name
"""
)

for users in cursor.fetchall():
    print(users)

cursor.execute(
    """
    SELECT users.name, COUNT(orders.id)
    FROM users
    JOIN orders ON users.id = orders.user_id
    GROUP BY users.name
"""
)

for users in cursor.fetchall():
    print(users)