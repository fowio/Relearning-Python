#VAR:.3f - f = float, .3: How many decimal points (3)
#VAR:10 - 10 is the amount of spaces the variable can display
#VAR:010 - The empty spaces will be padded with 0

price1 = 3.14159
price2 = 24.99
price3 = -9.111231

print(f"Price 1 is: ${price1:<10}") # Left justified
print(f"Price 2 is: ${price2:>10}") # Right justified
print(f"Price 3 is: ${price3:^10}") # Centered