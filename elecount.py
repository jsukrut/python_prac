lst1 = [1,2,2,3,3,4,5,5,5,6,6]


new_list =[]

for ele in lst1:
    count = 0
    for next_ele in lst1:
        if ele == next_ele:
            count += 1

    if count ==1:
        new_list.append(ele)
print(new_list)


print([ ele for ele in lst1 if lst1.count(ele) ==1 ])

