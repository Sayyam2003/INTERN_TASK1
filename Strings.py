def username_builder():
    print("\n--- Username Builder ---")
    full_name = input("Enter your full name: ").strip()
    
    # Build username: first letter of first name + last name, all lowercase
    parts = full_name.split()
    if len(parts) < 2:
        print("Please enter at least first and last name.")
        return
    
    username = parts[0][0].lower() + parts[-1].lower()
    print(f"Generated username: {username}")

def vowel_consonant_counter():
    print("\n--- Vowel and Consonant Counter ---")
    text = input("Enter a string: ").lower()
    
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")

if __name__ == "__main__":
    username_builder()
    vowel_consonant_counter()
