"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
"""
while True:
	print("Welcome to Rock-Paper-Scissors")
	print("There can only be one winner and one loser.")
	print("(Valid Inputs: R-Rock, P-Paper, S-Scissors)")
	p1 = input("\nPlayer 1's turn, please state your move: ")
	p2 = input("Player 2's turn, please state your move: ")
	
	correct_ins = ["R", "P", "S"]
	if p1 not in correct_ins or p2 not in correct_ins:
		print("Invalid input!")
	elif p1 == p2:
		print("It's a Draw.")
	elif p1 == "R":
		if p2 == "S":
			print("Player 1 wins")
		else:
			print("Player 2 wins")
	elif p1 == "S":
		if p2 == "P":
			print("Player 1 wins")
		else:
			print("Player 2 wins")
	elif p1 == "P":
		if p2 == "R":
			print("Player 1 wins")
		else:
			print("Player 2 wins")
		
	check = input("\nWould you like to start a new game? (y/n) ")
	if check == 'y' or check == 'yes' or check == 'Y':
		print("\n\n\n")
		continue
	else:
		print("Thank you for playing.")
		break
	
