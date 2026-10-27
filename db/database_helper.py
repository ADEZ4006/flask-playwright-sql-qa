import sqlite3

class DatabaseHelper:
    def buscar_usuario_por_email(self, email):
        conn = sqlite3.connect("tienda.db")
        cursor = conn.cursor()
        cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
        )
        fila = cursor.fetchone()
        conn.close()
        return fila
    def borrar_usuario_por_email(self, email):
        conn = sqlite3.connect("tienda.db")
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE email = ?",
            (email,)
        )
        conn.commit()
        conn.close()