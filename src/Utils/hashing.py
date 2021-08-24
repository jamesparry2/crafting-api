import hashlib

def hash_password_with_salt(password, salt):
    return hashlib.sha256(password + salt).hexdigest()