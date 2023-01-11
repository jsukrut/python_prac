# Python code to demonstrate
# call by reference
def add_more(list):
    list.append(50)
    print("Inside Function", list)

mylist = [10, 20, 30, 40]

add_more(mylist)
print("Outside Function:", mylist)