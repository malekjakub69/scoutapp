import pytest
from app import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def access_token(client):
    # URL pro přihlášení
    login_url = "/login"

    # Přihlašovací údaje
    login_data = {"username": "admin", "password": "Password1"}

    # Odeslat požadavek na přihlášení
    response = client.post(login_url, data=login_data)

    # Zkontrolovat, zda bylo přihlášení úspěšné
    assert response.status_code == 200

    # Získat přístupový token z odpovědi
    token = response.json().get("access_token")

    return token
