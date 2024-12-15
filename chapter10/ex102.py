fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

hours = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if words[0] == 'From' and ':' in word:
             hours[word.split(':')[0]] = hours.get(word.split(':')[0], 0) + 1
#print(hours)

l = list()

for k, v in hours.items():
    l.append( (k, v) )

l.sort()
for item in l:
    print(item)
