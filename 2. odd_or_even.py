"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Enter a number: "))
check = int(input("Enter the number to check: "))

"""
if num % 4 == 0:
	print("The number is a multiple of 4.")
elif num % 2 == 0:
	print("The number is an even number.")
else:
	print("The number is an odd number.")
"""

if num % check == 0:
	print(check, "divides evenly into", num)
else:
	print(check, "does NOT divide evenly into", num)
