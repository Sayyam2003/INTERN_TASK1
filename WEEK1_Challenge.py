#CLI Unit Converter: length, weight, temperature menus + loops & conditionals.

def convert_length():
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} meters = {value * 3.28084:.2f} feet")
    elif choice == "2":
        print(f"{value} feet = {value / 3.28084:.2f} meters")
    else:
        print("Invalid option.")

def convert_weight():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} kg = {value * 2.20462:.2f} lb")
    elif choice == "2":
        print(f"{value} lb = {value / 2.20462:.2f} kg")
    else:
        print("Invalid option.")

def convert_temperature():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")
    value = float(input("Enter temperature: "))

    if choice == "1":
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == "2":
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    else:
        print("Invalid option.")

def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Convert Temperature")
        print("4. Exit")

        option = input("Choose an option (1-4): ")

        if option == "1":
            convert_length()
        elif option == "2":
            convert_weight()
        elif option == "3":
            convert_temperature()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
