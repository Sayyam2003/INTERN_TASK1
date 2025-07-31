def multiplication_table():
    print("\n--- Multiplication Table ---")
    num = int(input("Enter a number: "))
    limit = int(input("Enter the range (e.g., 10): "))

    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")

def sum_divisible_by_3():
    print("\n--- Sum of Numbers Divisible by 3 ---")
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    total = sum(i for i in range(start, end + 1) if i % 3 == 0)
    print(f"Sum of numbers divisible by 3 from {start} to {end}: {total}")

if __name__ == "__main__":
    multiplication_table()
    sum_divisible_by_3()
