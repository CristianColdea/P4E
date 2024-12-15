"""
Exercise 6_1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards. 
"""

#input from the user
input_string = input('Please enter a string: ') 

#index for backwards
b_indx = len(input_string) - 1
#print(len(input_string))

#everything inside the loop ...
while b_indx >= 0:
    letter = input_string[b_indx]
    print(letter)
    b_indx -= 1
