"""
Exercise 5_1: Write a program which repeteadly reads numbers until the user
enters "done". Once "done" is entered, print out the total, count, and average
numbers. If the user enters anything other that a number, detect their mistake
using try and except and print an error message and skip to the next number.
"""

#accumulation variable
sum = 0

#counter
n = 0

#everything inside the loop ...
while True:
    user_input = input('Please enter a number: ')
    if user_input == 'done':
        break

    try:
        float_input = float(user_input)
    except:
        print('Please enter a number')
        continue

    sum = sum + float_input
    n += 1

print('Total of numbers entered is: ', sum)
print('You entered ',n, 'numbers')
print('Average of the entered number is: ', sum/n)
