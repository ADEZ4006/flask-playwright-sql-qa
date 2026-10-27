from playwright.sync_api import sync_playwright,Page, expect
from db.database_helper import DatabaseHelper

helper = DatabaseHelper()

def test_user_registration(page: Page) -> None:
	page.goto("http://127.0.0.1:5000/")

	search_input = page.locator('input[name="name"]')
	search_input.fill("Prueba Test")
	search_input = page.locator('input[name="email"]')
	search_input.fill("prueba@test.com")
	
	
	page.get_by_role("button", name="REGISTRAR").click()
	
	expect(page.get_by_text("Usuario registrado")).to_be_visible()
	fila = helper.buscar_usuario_por_email("prueba@test.com")
	assert fila is not None
	assert fila[1] == "Prueba Test"
	helper.borrar_usuario_por_email("prueba@test.com")