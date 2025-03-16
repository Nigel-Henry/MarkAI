from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import secrets
import string
from cryptography.fernet import Fernet

def generate_api_key():
    """
    Generate a random API key.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(32))

# AES encryption key (must be 16/24/32 bytes)
aes_key = b'SixteenByteKey123'
aes_iv = b'InitializationVec'

def aes_encrypt_data(data):
    """
    Encrypt data using AES-256.
    """
    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()

def aes_decrypt_data(encrypted_data):
    """
    Decrypt data using AES-256.
    """
    encrypted = base64.b64decode(encrypted_data)
    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode()

def fernet_encrypt_data(data):
    """
    Encrypt data using Fernet.
    """
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data, key

def fernet_decrypt_data(encrypted_data, key):
    """
    Decrypt data using Fernet.
    """
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data