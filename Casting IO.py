def average_of_three():
    print("\n--- Average of Three Numbers ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    
    avg = (a + b + c) / 3
    print(f"Average: {avg}")

def convert_minutes():
    print("\n--- Convert Minutes to Hours and Minutes ---")
    total_minutes = int(input("Enter total minutes: "))
    
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")

if __name__ == "__main__":
    average_of_three()
    convert_minutes()
