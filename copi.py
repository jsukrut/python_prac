import copy
#
l1 = [1,2,3,4,[5,6]]
l2 = copy.copy(l1)

print("l1",l1)
print("l2",l2)

l1[0]=4
l1[4][0]=67

print("l1",l1)
print("l2",l2)
