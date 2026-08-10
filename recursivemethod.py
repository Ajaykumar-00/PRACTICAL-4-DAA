# Steps 2 & 3: Recursive function to calculate factorial
def factorial_recursive(n):
    # Step 2: If n is 0 or 1, return 1 (Base Case)
    if n == 0 or n == 1:
        return 1

    # Step 3: Otherwise, return n * factorial(n - 1) (Recursive Step)
    return n * factorial_recursive(n - 1)


# Step 1: Start the program and read the value of n
if __name__ == "__main__":
    n = 7  # Example value for n

    print(f"Calculating recursive factorial for n = {n}")

    # Step 4: Display the factorial value returned by the recursive function
    result = factorial_recursive(n)
    print(f"Factorial of {n} is: {result}")

    # Step 5: Stop the program / Print Enrollment Number
    print("Enrollment number:92460118193")
