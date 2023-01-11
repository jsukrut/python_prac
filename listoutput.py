def f1(x,my_list =[]):
    my_list.append(x)
    return my_list

print(f1(10))
print(f1(20,[]))
print(f1(30))