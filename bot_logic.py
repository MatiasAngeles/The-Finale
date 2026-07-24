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
    """AnnoyinBot"""
    if message > 50:
        return "I just want peace, not commands."
    if message > 15:
        return "Yes I'm fine, I just don't want the user to talk to me."
    return "I don't want to do what the user needs..."


def ecosystem(comands: int) -> str:
    """HelpeRBoT"""
    if comands > 10:
        return "Now the user knows about the ecosystem!"
    if comands > 2:
        return "The user knows a little bit, needs to know more!"
    return "The user needs to know about the ecosystem!"


def list(message: int, comands: int) -> str:
    """ListyBot"""
    total = message + comands
    if total == 0:
        return "I guess the user is not necesarry for it."

    ratio = comands / total
    if ratio > 0.4:
        return "The user"
    if message > 30:
        return "Chatty profile detected. Low command-to-message ratio."
    return "Standard user profile. Activity levels are nominal."
    
