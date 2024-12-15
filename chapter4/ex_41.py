"""
Rewrite pay computation with time-and-a-half for overtime and create a function
'computepay' which takes two parameters ('hours' and 'rate').
"""

#check for the appropriate input
input_time = input('Please enter the work hours: ')
input_rate = input('Please enter the work rate: ')

#hours
try:
    time = float(input_time)
except:
    print('Please enter numerical hours.')
    quit()

#rate
try:
    rate = float(input_rate)
except:
    print('Please enter numerical rate.')
    quit()

#define the function
def computepay(hours, rate):
    if hours > 40:
        return ((hours - 40) * 0.5 * rate + hours * rate)
    else:
        return hours * rate

#call the function and print the result
print('Pay is: ', computepay(time, rate))
