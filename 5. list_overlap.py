import random
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this

2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for num_a in a:
	if num_a in b:
		c.append(num_a)
c = set(c)
print(c)



print("\n\n\n")
# Extras 2.
print(set(list(num for num in a if num in b)))



print("\n\n\n")
# Extras 1.
a = list(random.randrange(i) for i in range(2,100))
b = list(random.randrange(i) for i in range(2,100))
c = []
for num_a in a:
	if num_a in b:
		c.append(num_a)
c = set(c)
print(c)


















