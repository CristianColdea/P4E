import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:    
             counts[letter] = counts.get(letter, 0) + 1
#print(counts)

l = list()

for k, v in counts.items():
    l.append( (k, v) )

l.sort()
for item in l:
    print(item[0],f"{item[1]/sum(counts.values()) :.2%}")
