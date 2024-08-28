import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\|}{~:]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    
    strength = {
        0: "Strong",
        1: "Moderate",
        2: "Weak",
        3: "Very Weak",
        4: "Extremely Weak",
        5: "Invalid"
    }
    
    return strength[sum(errors)]

# Example Usage
password = input("Enter your password: ")
print(f"Password Strength: {check_password_strength(password)}")
