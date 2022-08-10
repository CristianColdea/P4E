fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dow = dict()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for line in fhand:
    words = line.split()
    for word in words:
        if word in days:
            dow[word] = dow.get(word, 0) + 1

print(dow)
