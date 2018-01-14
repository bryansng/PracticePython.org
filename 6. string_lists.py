"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
string = input("Enter a string to check if it is a palindrome:\n")
string = string.lower()
for i in range(len(string)):
	if not string[i] == string[len(string) - i - 1]:
		print("\nThe string is NOT a palindrome.")
		break
	if i == len(string) - 1:
		print("\nThe string is a palindrome.")
	
print("\n\n")	
# OR
word = input("Please enter a word:\n")
rvs = word[::-1]
if word == rvs:
	print("\nThis word is a palindrome.")
else:
	print("\nThis word is NOT a palindrome.")
