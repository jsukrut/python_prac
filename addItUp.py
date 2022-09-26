
def add_it_up(val):
    sum_up = 0
    if isinstance(val,int):
        for no in range(1,val):
            sum_up+=no
        return  sum_up
    else:
        return sum_up


print(add_it_up(5))
