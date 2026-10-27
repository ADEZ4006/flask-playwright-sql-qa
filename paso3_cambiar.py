import sqlite3

conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE users SET email = ? WHERE email = ?",('juan_new@email.com', 'juan@email.com')
)
conn.commit()

cursor.execute("SELECT * FROM users WHERE email = 'juan_new@email.com'")
updt = cursor.fetchone()
print(f"1 - user found: {updt}\n")

cursor.execute(
    "DELETE FROM users WHERE email = 'maria@email.com'"
)
conn.commit()

cursor.execute("SELECT * FROM users")
for users in cursor.fetchall():
    print(users)

conn.close()