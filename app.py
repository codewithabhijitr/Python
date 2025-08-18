# Multiplication table program

# Take input from user
num = int(input("Enter a number: "))

# Print table from 1 to 10
print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
