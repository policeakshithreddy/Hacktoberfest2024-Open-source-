import re

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Evaluate password strength
    if all([length_criteria, uppercase_criteria, lowercase_criteria,
            digit_criteria, special_char_criteria]):
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (digit_criteria or special_char_criteria):
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
