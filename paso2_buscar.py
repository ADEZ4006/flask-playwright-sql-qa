import sqlite3

conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE email = 'ana@email.com'")
spe_user = cursor.fetchone()
print(f"1 - user found: {spe_user}\n")

cursor.execute("SELECT * FROM users ORDER BY name")
order_list = cursor.fetchall()
print(f"2 - user found: {order_list}\n")

cursor.execute("SELECT * FROM users WHERE name LIKE '%ez%'")
last_names = cursor.fetchall()
print(f"3 - user found: {last_names}\n")

conn.close()