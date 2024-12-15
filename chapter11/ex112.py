import re

hand = open('mbox-short.txt')

sum = 0
cnt = 0
for line in hand:
    line = line.rstrip()
    y = re.findall('^New Revision: ([0-9]+)', line)
    if len(y) > 0:
        sum = sum + int(y[0])
        cnt +=  1

#print(sum, cnt)
print(int(sum/cnt))
