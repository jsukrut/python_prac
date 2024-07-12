'''
*
* *
* * *
* * * *
* * * * *
'''


for row in range(0,6):
    for column in range(0,row):
        print("*",end=" ")
    print("")


'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

count = 1
for row in range(0,6):
    for column in range(0,row):
        print(count ,end=" ")
        count += 1
    print("")

'''
2
4 6
8 9 10
12 14 16 20
22 24 26 28 30
'''

count = 1
no = 2
for row in range(0,6):
    for column in range(0,row):
        print(no*count ,end=" ")
        count = count + 1
    print("")

'''
A
B C
D E F
G H I J
K L M N O
'''

count = 65
for row in range(0,6):
    for column in range(0,row):
        print(chr(count) ,end=" ")
        count += 1
    print("")


'''
a
b c
d e f
g h i j
k l m n o
'''

count = 97
for row in range(0,6):
    for column in range(0,row):
        print(chr(count) ,end=" ")
        count += 1
    print("")


'''
z
y x
w v u
t s r q
p 0 n m l
'''
3
count = 97+25
for row in range(0,6):
    for column in range(0,row):
        print(chr(count) ,end=" ")
        count -= 1
    print("")
