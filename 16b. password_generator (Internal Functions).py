"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

- Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import string
import random

# string.printable
# OR
# string.ascii_letters + string.digits + string.punctuation

def get_pw(strength):
	ldp = string.ascii_letters + string.digits + string.punctuation
	if strength == 1:
		return "".join(random.sample(ldp, random.randint(5, 10)))
	elif strength == 2:
		return "".join(random.sample(ldp, random.randint(10, 20)))
	elif strength == 3:
		return "".join(random.sample(ldp, random.randint(20, 30)))
	else:
		pass

while True:		
	strength = int(input("Please enter the strength for the password: "))
	pw = get_pw(strength)
	print(pw, "\n\n\n")
	


























