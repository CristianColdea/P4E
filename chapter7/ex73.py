fname = input('Enter the file name: ')
#print(fname)
if fname == "na na boo boo":
    print("NA NA BOO BOO - You have been caught!")
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

sum = 0
count = 0

for line in fhand:
    line = line.rstrip()
    if line.find("X-DSPAM-Confidence") == -1: continue
    curr_coef = float(line[line.find(':')+1:])
    sum = sum+curr_coef
    count = count + 1

print("Average spam confidence is: ",sum/count)
