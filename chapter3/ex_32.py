"""
Exercise 3.2: Rewrite your pay program using try and except so that your program
handles non-numerical input gracefully by printing a message and exiting the
program.
"""

input_time = input('Enter hours: ')
input_rate = input('Enter rate: ')

# try-except for hours
try:
    time = float(input_time)
except ValueError:
    print('Error! Please enter a numerical time')
    quit()

# try-except for rate
try:
    rate = float(input_rate)
except ValueError:
    print('Error! Please enter a numerical rate')
    quit()

print('Pay: ', time*rate)
