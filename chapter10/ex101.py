fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

addresses = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if words[0] == 'From' and '@' in word:
#            addresses[word.split('@')[0]] = addresses.get(word.split('@')[0], 0) + 1
#            print(word.split('@'))
             addresses[word] = addresses.get(word, 0) + 1
#print(addresses)

l = list()

for k, v in addresses.items():
    l.append( (v, k) )

l.sort(reverse=True)
c, a = l[0]
print(a, c)
