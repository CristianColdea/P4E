nmb = 0
nlist = [] 

while nmb != 'done':
    nmb = input('Enter a number (type \"done\" to end): ')
    if nmb == 'done': break
    try:
        int(nmb)
        nlist.append(nmb)
    except:
        print(nmb, 'is not a number')

print('Maximum: ', max(nlist))
print('Minimum: ', min(nlist))
