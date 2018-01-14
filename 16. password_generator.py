"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

- Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random
words = "abcdefghijklmnopqrstuvwxyz1234567890!@$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gen_pw(codes, strength):
	if strength == 1:
		return "".join(random.sample(codes, random.randint(4, 10)))
	elif strength == 2:
		return "".join(random.sample(codes, random.randint(11, 20)))
	elif strength == 3:
		return "".join(random.sample(codes, random.randint(21, 30)))

while True:
	strength = int(input("Enter the strength (1-3) of your random password: "))
	pw = gen_pw(words, strength)
	print(pw)
	
	check = input("\n\nWould you like to continue (y/n): ")
	if check == "y":
		print("\n")
		continue
	else:
		break

























