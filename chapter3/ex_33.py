"""
Exercise 3.3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following correspondence:
Score    Grade
>= 0.9   A
>= 0.8   B
>= 0.7   C
>= 0.6   D
< 0.6    F
"""

#check for the proper input
score_input = input('Enter score: ')

try:
    score = float(score_input)
except:
    print('Please enter a numerical score.')
    quit()

#comply with a score between 0.0 and 1.0
while score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print('Grade is: A')
        quit()
    elif score >= 0.8:
        print('Grade is: B')
        quit()
    elif score >= 0.7:
        print('Grade is: C')
        quit()
    elif score >= 0.6:
        print('Grade is: D')
        quit()
    else:
        print('Grade is: F')
        quit()

#warn about wrong score interval and exit program
print('Score must be between 0.0 and 1.0')
