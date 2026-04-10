# Taking input from the user
a = input("Enter first number (a): ")
b = input("Enter second number (b): ")
c = input("Enter third number (c): ")

print(f"\nBefore swap: a = {a}, b = {b}, c = {c}")

# Swapping the values
# a gets b, b gets c, c gets a
a, b, c = b, c, a

print(f"After swap:  a = {a}, b = {b}, c = {c}")
