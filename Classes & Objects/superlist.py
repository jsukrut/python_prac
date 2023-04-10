class Superlist(list):
    def __len__(self):
        return 100

superlist1 = Superlist()
print(superlist1)
superlist1.append(5)
print(superlist1.__len__())
print(superlist1)

print(superlist1)
print(issubclass(Superlist,list))
