import secrets
import string

def generate_password(length=12, use_uppercase = True, use_digit = True, use_special = True):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digit = string.digits if use_digit else ''
    special = string.punctuation if use_special else ''

    all_str = lowercase + uppercase + digit + special

    if not all_str:
        raise ValueError("one character must be selected")
    
    if length < 1:
        raise ValueError("Must be minimum 1")
    
    if length > 50:
        raise ValueError("Max 50")

    chars = []
    for _ in range(length):
        chars.append(secrets.choice(all_str))
    
    password = ''.join(chars)
    return password