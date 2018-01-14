"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
""""

import datetime

#name  = input("Please enter your name: ")
#age = int(input("Please enter your age: "))
name = "Bryan"
age = 20
times = int(input("Enter the number of times to print the message: "))

year = int(datetime.date.today().strftime("%Y"))
year_age_100 = year + 100 - 20

msg = "Hello " + name + ", you will turn 100 in the year " + str(year_age_100) + "\n"
print(msg * 5)


