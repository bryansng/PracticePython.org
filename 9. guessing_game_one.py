import random
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

- Keep the game going until the user types “exit”
- Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
counter = 0
rand = random.randint(1, 9)
while True:
	num = input("Guess a number between 1 and 9: ")
	counter += 1
	
	if num == "exit":
		print("Thank you for playing.")
		break
		
	num = int(num)
	if num == rand:
		print("Your guess was exactly right.")
		print("Total Guesses:", counter)
		break
	elif num > rand:
		print("Your guess was greater than the number.")
	elif num < rand:
		print("Your guess was lower than the number.")
		
	print("\n")


























