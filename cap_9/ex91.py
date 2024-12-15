from random import *

wdict = {}

fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words: 
        wdict[word] = randint(1, 10)

print(wdict)

print('skills' in wdict)
