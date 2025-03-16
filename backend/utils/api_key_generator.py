import secrets
import string

def generate_api_key(length=32):
    """
    Generate a random API key.

    Parameters:
    length (int): The length of the API key. Default is 32.

    Returns:
    str: A randomly generated API key.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))