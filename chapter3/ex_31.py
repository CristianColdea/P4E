"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
rate for hours worked above 40 hour.

Enter hours: 45
Enter Rate: 10
Pay: 475
"""

# initialize variables
pay = 0.0

input_time = input('Enter hours: ')
input_rate = input('Enter rate: ')

# cast inputs to floats
time = float(input_time)
rate = float(input_rate)

if time <= 40:
    pay = time * rate
else:
    additional = time - 40
    pay = (rate * 40.0) + (1.5 * rate * additional)

print('The total pay is: ', pay)
