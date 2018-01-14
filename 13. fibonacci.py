"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def print_fibo_nums(num):
	f_2 = 1
	f_1 = 1
	if num >= 1:
		print(f_2)
	if num >= 2:
		print(f_1)
		
	for i in range(3, num+1):
		f = f_1 + f_2
		print(f)
		
		f_2 = f_1
		f_1 = f
		
num = int(input("Please enter the term of Fibonnaci numbers to display: "))
print_fibo_nums(num)
