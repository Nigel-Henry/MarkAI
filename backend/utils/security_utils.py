from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

# Function to encrypt data using Fernet symmetric encryption
def encrypt_data(data):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data, key

# Function to decrypt data using Fernet symmetric encryption
def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to hash a password using Werkzeug
def hash_password(password):
    return generate_password_hash(password)

# Function to verify a password against a hashed password using Werkzeug
def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)
