

def fibo(no):
    if no <=1:
        return 1
    else:
        return fibo(no-1)+fibo(no-2)

for i in range(15):
    print(fibo(i))