def test_get_users_401(client):
    response = client.get("/users")
    assert response.status_code == 401


def test_get_users(access_token, client):
    # Hlavička s přístupovým tokenem
    headers = {"Authorization": f"Bearer {access_token}"}

    # Odeslat požadavek na endpoint
    response = client.get("/users", headers=headers)

    # Zkontrolovat, zda byl požadavek úspěšný
    assert response.status_code == 200
