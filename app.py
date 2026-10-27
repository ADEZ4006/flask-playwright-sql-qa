import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/")
def home():
	return '''
	<form method="POST" action="/registrar">
		<input type="text" name="name"><br>
		<input type="text" name="email"><br>
		<button type="submit">REGISTRAR</button>
	</form>
	'''
@app.route("/registrar", methods=["POST"])
def registrar():
	name = flask.request.form["name"]
	email = flask.request.form["email"]
	conn = sqlite3.connect("tienda.db")
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO users (name, email) VALUES (?, ?)",
		(name, email),
	)
	conn.commit()
	return "Usuario registrado"

if __name__ == "__main__":
	app.run(debug=True)