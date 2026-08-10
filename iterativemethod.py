def factorial_iterative(n):
    # Step 2: Initialize a variable fact = 1
    fact = 1

    # Step 3: Repeat from 1 to n, multiplying fact by each number
    for i in range(1, n + 1):
        fact *= i

    # Step 4: Display the factorial value
    return fact


# Step 1: Start the program and read the value of n
if __name__ == "__main__":
    n = 5  # Example value for n

    print(f"Calculating factorial for n = {n}")
    result = factorial_iterative(n)

    # Step 4: Display the factorial value
    print(f"Factorial of {n} is: {result}")

    # Step 5: Stop the program
    print("Enrollment number:92460118193")
