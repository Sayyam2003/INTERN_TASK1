def main():
name = input("Enter your name: ")
print(f"Hello, my name is {Sayyam}.")

if __name__ == "__main__":
main()\
    
# This will fail because:
The lines inside the main() function are not indented.

The main() call under if __name__ == "__main__" is also not indented.

# Lines inside main() are indented with 4 spaces.

The main() call under the if __name__ == "__main__" block is also indented correctly.
#now fix indented code will be:

def main():
    name = input("Enter your name: ")
    print(f"Hello, my name is {Sayyam}.")

if __name__ == "__main__":
    main() 
    