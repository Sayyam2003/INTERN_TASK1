import re

def grade_calculator():
    print("\n--- Grade Calculator ---")
    marks = float(input("Enter your marks (0-100): "))
    
    if marks < 0 or marks > 100:
        print("Invalid marks entered.")
        return
    
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Your grade is: {grade}")

def password_strength(password):
    length = len(password)
    strength = 0
    
    # Check length
    if length >= 8:
        strength += 1
    # Has lowercase
    if re.search(r'[a-z]', password):
        strength += 1
    # Has uppercase
    if re.search(r'[A-Z]', password):
        strength += 1
    # Has digit
    if re.search(r'\d', password):
        strength += 1
    # Has special char
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"

def password_strength_classifier():
    print("\n--- Password Strength Classifier ---")
    pwd = input("Enter your password: ")
    result = password_strength(pwd)
    print(f"Password strength: {result}")

if __name__ == "__main__":
    grade_calculator()
    password_strength_classifier()
