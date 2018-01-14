"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

- Write two different functions to do this - one using a loop and constructing a list, and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
a = [1, 1, 2, 3, 4, 4, 5, 6, 7, 10]

def rmv_duplicates_via_sets(a):
	return list(set(a))

a = rmv_duplicates_via_sets(a)
print(a)



print("\n\n\n")
# Extra
a = [1, 1, 2, 3, 4, 4, 5, 6, 7, 10]

def rmv_duplicates_via_loops(a):
	b = []
	for num in a:
		if num not in b:
			b.append(num)
	return b
	
a = rmv_duplicates_via_loops(a)
print(a)












