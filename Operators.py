def bmi_calculator():
    print("\n--- BMI Calculator ---")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

def simple_interest_calculator():
    print("\n--- Simple Interest Calculator ---")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    
    interest = (principal * rate * time) / 100
    print(f"Simple Interest: {interest:.2f}")

if __name__ == "__main__":
    bmi_calculator()
    simple_interest_calculator()
