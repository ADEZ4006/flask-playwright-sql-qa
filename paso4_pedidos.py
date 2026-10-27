import sqlite3

conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    price REAL
    )
"""
)

new_orders = [
    (1, "Burrito", 5.46),
    (2, "Taco", 3.25),
    (3, "Pizza", 12.99),
]

cursor.executemany(
    "INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)",
    new_orders,
)
conn.commit()

cursor.execute(
    "UPDATE orders SET user_id = 1 WHERE product = 'Taco'"
)
conn.commit()

cursor.execute(
    """
    SELECT users.name, orders.product, orders.price
    FROM users
    JOIN orders ON users.id = orders.user_id
"""
)

for users in cursor.fetchall():
    print(users)

conn.close()
