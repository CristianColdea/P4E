fname = input('Enter the file name: ')
fhand = open(fname)
wlist = []
for line in fhand:
    words = line.split()
    for word in words:
        if word in wlist: continue
        else: wlist.append(word)

wlist.sort()
print(wlist)
