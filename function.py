import re
def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Regular expressions to check password strength
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*()\-_=+]', password)

    # Conditions to determine password strength
    if not has_upper:
        return "Weak: Password must include at least one uppercase letter."
    if not has_lower:
        return "Weak: Password must include at least one lowercase letter."
    if not has_digit:
        return "Weak: Password must include at least one number."
    if not has_special:
        return "Weak: Password must include at least one special character (!@#$%^&*()-_+=)."

    return "Strong: Your password is secure!"

# Example Usage
password = input("Enter your password: ")
print(check_password_strength(password))

# Filter for filtering out items from a list.

