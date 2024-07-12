row = int(input("Please enter no of rows"))
no =1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(no,end="")
        no+=2
    print()
