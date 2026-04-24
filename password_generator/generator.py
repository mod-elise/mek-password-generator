import secrets
import math


def calculateStrength(pw_length, pool_length):
    entropy = pw_length * math.log2(pool_length)
    if entropy < 40:
        return "Weak"
    elif entropy <= 60:
        return "Medium"
    else:
        return "Strong"


def secureShuffle(inputList):
    shuffledList = []
    while len(inputList) > 0:
        position = secrets.randbelow(len(inputList))
        char = inputList.pop(position)
        shuffledList.append(char)
    return shuffledList


def generate_pools():
    # separate function so that custom pools might be possible - or an option to remove ambigous characters like 'l' and '1' in the future
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return lower_case, upper_case, digits, symbols


def generate_password(pw_length, use_upper, use_digits, use_symbols):
    lower_case, upper_case, digits, symbols = generate_pools()
    selected_pools = [lower_case]
    combined_pool = ""
    password_chars = []

    if use_upper:
        selected_pools.append(upper_case)

    if use_digits:
        selected_pools.append(digits)

    if use_symbols:
        selected_pools.append(symbols)

    # Put at least 1 char from each selected pool into the password
    for pool in selected_pools:
        password_chars.append(secrets.choice(pool))
        combined_pool = combined_pool + pool

    # Add the rest of the characters
    remaining_length = pw_length - len(password_chars)
    for i in range(remaining_length):
        password_chars.append(secrets.choice(combined_pool))

    securePassword = "".join(secureShuffle(password_chars))
    password_strength = calculateStrength(pw_length, len("".join(combined_pool)))
    return securePassword, password_strength
