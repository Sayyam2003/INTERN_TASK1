def collect_user_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))

    print("\n--- Profile Summary ---")
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")

def swap_variables():
    print("\n--- Swap Two Variables ---")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    
    print(f"Before swap: a = {a}, b = {b}")
    
    a, b = b, a  # swap without temp variable
    
    print(f"After swap: a = {a}, b = {b}")

if __name__ == "__main__":
    collect_user_profile()
    swap_variables()