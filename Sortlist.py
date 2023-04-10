

l1 =[45,61.3,56,61.2,3,10,1,5]
length=len(l1)
print(l1)
for no in range(length):
    for next_no in range(no+1,length):
        if l1[no] > l1[next_no]:
            temp = l1[no]
            l1[no] = l1[next_no]
            l1[next_no] = temp
print(l1)


