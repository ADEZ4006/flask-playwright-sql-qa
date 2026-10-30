# Registration app in Flask + Automation test with Playwright and SQL

![Tests](https://github.com/ADEZ4006/flask-playwright-sql-qa/actions/workflows/test.yml/badge.svg)

## What it does

The app saves users in SQLite via web; the test registers a user on the page, verifies the row directly
in the database and cleans up after itself with a DELETE.

The tienda.db database is not included in the repo (it's in .gitignore)-- create it locally first; the
app and the test use the users table.

## Tech stack

- Python
- Flask
- SQLite
- Playwright
- Pytest
- Docker
- Requests

## How to run

`pip install -r requirements.txt`
`playwright install`
`python app.py` -- in one terminal.
`pytest` -- in a different terminal.

Run it in Docker -- the SQLite database lives in a named volume, so it survives container deletion:

docker build -t flask-sql-app .
docker volume create tienda-data
docker run -p 5000:5000 -v tienda-data:/app flask-sql-app

## API tests

The Flask app's endpoints are also tested directly over HTTP with `requests` and pytest (no browser),
in `test_api.py`:
- `GET /` returns 200
- `POST /registrar` with a name and email returns 200 and the success message; the test deletes the created user 
afterwards.
- A registered user is verified in the SQLite database through the `DatabaseHelper` class, then removed and
confirmed gone.
- Know defect: `POST /registrar` without an email should return 400 but currently returns 500. The test is marked
`xfail` until the app validates missing fields.

## Project structure

`app.py` -- the Flask app: registration form and the route that saves users.
`db/database_helper.py` -- helper with the SQL queries (find and delete a user by email, parameterized).
`tests/test_user_registration.py` -- the Playwright end-to-end test.
`conftest.py` -- pytest configuration at the project root.
`paso1` to `paso5` scripts -- my SQL practice scripts (create the database, queries, orders, summary).
`test_api.py` -- the API test for the Flask app, with requests and pytest.