def chop(lst):
#    print(len(lst))
    del lst[0]
#    print(len(lst))
    del lst[len(lst)-1]

t = ['a', 'b', 'c', 'd', 'e']
t3 = t
print(t3)

chop(t)

print(t)
print(t3)

def middle(lst):
    lst2 = lst[1:-1]
    return lst2

t2 = ['a', 'b', 'c', 'd', 'e']
print(middle(t2))
