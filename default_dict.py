
from collections import defaultdict

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

counter = defaultdict(list)
for no in myList:
    counter[no] = [0]

print(dict(counter))