"""
Exercise 5_2: Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead of
the average.
"""

#min variable
m = None

#max variable
M = None

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

    if m is None or float_input < m:
        m = float_input
    if M is None or float_input > M:
        M = float_input

print('Minimum is: ', m)
print('Maximum is: ',M)
