



term = int(input("Enter Term "))

fibo_series =[]

for no in range(term):
    print("term",no)
    if no <=1:
        fibo_series.append(no)
    else:
        fibo_no = fibo_series[no-1] + fibo_series[no-2]
        fibo_series.append(fibo_no)
    print(fibo_series)
print(fibo_series)






