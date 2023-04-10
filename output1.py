class C:
    dangerous = 2
c1 = C()
c2 = C()

print(id(C.dangerous))

print (c1.dangerous)
C.dangerous = 5

c1.dangerous =3

print (c1.dangerous)
print (c2.dangerous)

print (id(c1.dangerous))
print (id(c2.dangerous))



# del c1.dangerous
# print (c1.dangerous)
# C.dangerous = 3
# print (c2.dangerous)