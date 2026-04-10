# Get number of terms from the user
n = int(input("How many terms of Fibonacci series? "))

# Initializing the first two terms
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series up to {n} term: {a}")
else:
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        # Updating values: a becomes b, b becomes the sum
        a, b = b, a + b
        count += 1
