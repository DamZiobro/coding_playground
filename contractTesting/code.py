import requests


def user(user_name):
    """Fetch a user object by user_name from the server."""
    uri = 'http://localhost:1234/users/' + user_name
    return requests.get(uri).json()
