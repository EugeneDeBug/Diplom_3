import requests
from url import BASE_URL

def register_user(payload):
    return requests.post(f"{BASE_URL}/api/auth/register", json=payload)

def delete_user(access_token):
    return requests.delete(
        f"{BASE_URL}/api/auth/user",
        headers={"Authorization": access_token}
    )
