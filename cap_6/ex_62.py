"""
Exercise 6_2: Write a program with a function to take as arguments a string and
a letter in order to count the occurence of the letter within the string.
"""

#define the count function
def count(word, letter):
    cnt = 0
    for item in word:
        if item == letter:
            cnt += 1
    print(cnt)

#input from the user
input_string = input('Please enter a string: ')
character = input('Please enter a letter to check for: ')

#call the function count upon user input
count(input_string, character)
