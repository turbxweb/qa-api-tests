import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_success():
     # Test retrieving existing user 
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "username" in data


def test_get_user_not_found():
    #Test API response for non-existing user
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404





def test_user_has_email():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    assert "email" in data