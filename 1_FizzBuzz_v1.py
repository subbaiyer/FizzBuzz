# Fizzbuzz Project: Unit 1: Beginner's Python
# Author: R Prasana Venkateswaran

# With extra challenge

import numbers

# Get input from user
running = True

while (running):
    N = input("Enter a number between 1 and 200: ")

    # Check if you have a number
    if N <= 0 or N > 200:
        print("Re-enter the number. It should be an integer between 1 and 200!")
        running = True
    else:
        running = False
 
# Print Fizz/Buzz for the given input
for n in range(1,N):
    if ((n % 3 == 0) and (n % 5 == 0)):
        print("fizzbuzz")
    elif n % 3 == 0: 
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else: 
        print(n)


