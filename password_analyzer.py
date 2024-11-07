import re

# Load common passwords from file
def load_common_passwords(file_path="common_passwords.txt"):
    with open(file_path, "r") as file:
        common_passwords = {line.strip() for line in file}
    return common_passwords

# Function to analyze password strength
def analyze_password_strength(password, common_passwords):
    strength_score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password is too short, should be at least 8 characters.")

    # Check for mixed case, digits, and special characters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("Include numbers in your password.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("Add special characters like !@#$%^&* for better strength.")

    # Check against common passwords list
    if password in common_passwords:
        feedback.append("Password is too common. Avoid using easily guessable passwords.")
        strength_score = max(0, strength_score - 2)  # Reduce score if common

    # Provide strength evaluation
    if strength_score >= 5:
        return "Strong", feedback
    elif strength_score >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

if __name__ == "__main__":
    common_passwords = load_common_passwords()
    password = input("Enter a password to analyze: ")
    strength, feedback = analyze_password_strength(password, common_passwords)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for tip in feedback:
            print(f"- {tip}")
