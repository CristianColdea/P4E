fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

domains = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if words[0] == 'From' and '@' in word:
            domains[word.split('@')[1]] = domains.get(word.split('@')[1], 0) + 1

print(domains)
