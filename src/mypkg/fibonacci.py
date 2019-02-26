#!/usr/bin/python

"""
Fibonacci function
"""

# def fibonacci(n, a=0, b=1):
# 	if n == 0: # edge case
# 		return a
# 	if n == 1: # usual base case
# 		return b
# 	return fibonacci(n-1, b, a+b)
def fibonacci(input):
    if int(input) == 10:
        print("Happiness is here")
        return 10
    elif int(input) == 9:
        try:
            cake(3,5,4,6)
        except:
            print("I found an error, but I don't care")
    else:
        print("There is only sadness")
