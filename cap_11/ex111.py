import re

hand = open('mbox-short.txt')

to_search = input('Enter a regular expression:')

cnt = 0
for line in hand:
    line = line.rstrip()
    if re.search(to_search, line):
        cnt += 1

print('mbox-short.txt had', cnt, 'that matched', to_search)
cnt = 0
