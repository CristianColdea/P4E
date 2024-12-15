"""
Exercise 4.7: Rewrite the grade program from previous chapter using a function
called 'computegrade' that takes a score as its parameter and returns a grade as
a string.
Score    Grade
>= 0.9   A
>= 0.8   B
>= 0.7   C
>= 0.6   D
<0.6     F
"""

#check for the appropriate input
score_input = input('Please enter the score: ')

try:
    score = float(score_input)
except:
    print('The score must be numerical.')
    quit()

#define 'computegrade' function
def computegrade(score):
    while score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            return 'The grade is: A'
        elif score >= 0.8:
            return 'The grade is: B'
        elif score >= 0.7:
            return 'The grade is: C'
        elif score >= 0.6:
            return 'The grade is: D'
        else:
            return 'The grade is: F'
    return 'The score must be between 0.0 and 1.0'

#call the function and print the result
print(computegrade(score))
