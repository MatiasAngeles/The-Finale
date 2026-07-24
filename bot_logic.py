import requests
from settings import API_URL


def activity(user_id: str, username: str, accion: str) -> bool:
    """Registers the message/command activity into the backend."""
    payload = {"username": username, "action_type": accion}
    try:
        response = requests.post(
            f"{API_URL}/users/{user_id}/activity", json=payload, timeout=5
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as error:
        print(f"API has failed because: {error}")
        return False


def get_user_data(user_id: str) -> dict:
    """Gets the user activity from the server."""
    try:
        response = requests.get(f"{API_URL}/users/{user_id}", timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as error:
        print(f"API has failed because: {error}")
    return {}


def annoyed(message: int) -> str:
    """1"""
    if message > 50:
        return "text."
    if message > 15:
        return "text"
    return "text"


def ecosystem(comands: int) -> str:
    """2"""
    if comands > 10:
        return "text"
    if comands > 2:
        return "text"
    return "text"


def list(message: int, comands: int) -> str:
    """3"""
    total = message + comands
    if total == 0:
        return "text"

    ratio = comands / total
    if ratio > 0.4:
        return "The user"
    if message > 30:
        return "text"
    return "text."
    
