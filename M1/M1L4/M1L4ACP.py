# Get input from the user
num = int(input("Enter a number: "))

# Convert to string to easily count digits and iterate
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of digits raised to the power of the number of digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the sum matches the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
