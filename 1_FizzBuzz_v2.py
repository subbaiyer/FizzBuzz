# Fizzbuzz Project: Unit 1: Beginner's Python
# Author: R Prasana Venkateswaran
# Code version # 2
# With extra challenge

import sys
import numbers

if len(sys.argv) == 1:
    n = int(float(input("Enter a number: ")))
else:
    try:
        n = int(float(sys.argv[1]))
    except ValueError:
        n = int(float(input("That is not a valid entry.  Please enter a number: ")))
    except NameError:
        n = int(float(input("That is not a valid entry.  Please enter a number: ")))

 
# Print Fizz/Buzz for the given input
for k in range(1,n):
    if ((k % 3 == 0) and (k % 5 == 0)):
        print("fizzbuzz")
    elif k % 3 == 0: 
        print("fizz")
    elif k % 5 == 0:
        print("buzz")
    else: 
        print(k)