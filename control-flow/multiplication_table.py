# multiplication_table.py

# Prompt the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 10 + 1):
    product = number * i
    print(f"{number} * {i} = {product}")
