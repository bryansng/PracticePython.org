"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
  
Then I would see the string:

  Michele is name My
  
shown back to me.
"""
words = "My name is Michele"

def reverse_v1(a):
	#a = a.split(" ")
	return " ".join(a.split(" ")[::-1])
	
def reverse_v2(a):
	#a = a.split(" ")
	return " ". join(reversed(a.split(" ")))
	
def reverse_v3(a):
	a = a.split(" ")
	a.reverse()
	return " ".join(a)
	
def reverse_v4(a):
	a = a.split(" ")
	b = []
	for word in a:
		b.insert(0, word)
	return " ".join(b)

print(reverse_v1(words))
print(reverse_v2(words))
print(reverse_v3(words))
print(reverse_v4(words))

















