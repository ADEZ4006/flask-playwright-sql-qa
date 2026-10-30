import requests
from db.database_helper import DatabaseHelper
import pytest

def test_home_retorna_200():
    resp = requests.get("http://localhost:5000/")
    assert resp.status_code == 200

def test_registrar_retorna_200():
    regis = {"name": "Api", "email": "api@test.com"}
    resp = requests.post("http://localhost:5000/registrar", data= regis)
    assert resp.status_code == 200
    assert "Usuario registrado" in resp.text
    db = DatabaseHelper()
    db.borrar_usuario_por_email("api@test.com")

def test_registrar_guarda_en_base():
    regis = {"name": "Api", "email": "api@test.com"}
    resp = requests.post("http://localhost:5000/registrar", data= regis)
    db = DatabaseHelper()
    fila = db.buscar_usuario_por_email("api@test.com")
    assert fila is not None
    assert fila[2] == "api@test.com"
    db.borrar_usuario_por_email("api@test.com")
    fila = db.buscar_usuario_por_email("api@test.com")
    assert fila is None

@pytest.mark.xfail(reason = "la app devuelve 500 cuando falta el email deberia de se 400")
def test_registrar_sin_email_retorna_400():
    resp = requests.post("http://localhost:5000/registrar", data={"name": "Api"})
    assert resp.status_code == 400