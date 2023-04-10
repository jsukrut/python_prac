
def fibo(no):
    no1 = 0
    no2 = 1
    sum = 0
    count =1
    while count <=no:
        print(sum," ",end='')
        count =count +1
        no1 =no2
        no2 =sum
        sum = no1+ no2

series = int(input("Enter No"))    
fibo(series)
