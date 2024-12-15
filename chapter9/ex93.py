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
            addresses[word] = addresses.get(word, 0) + 1

print(addresses)
