'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).'''


members =[]
for no in range(2000,32000):
    if no % 7 == 0 and no % 5 != 0:
        members.append(str(no))
print(','.join(members))