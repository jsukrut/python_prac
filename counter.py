
# counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

# counter = {}
# for no in myList:
# 	if no in counter.keys():
# 		counter[no] +=1
# 	else:
# 		counter[no] =1
# print(counter)


# Optimized 1 

# for no in myList:
# 	counter[no] = counter.get(no, 0) + 1

# print(counter)



# Optimized using collection 

from collections import Counter

counter = Counter(myList)

print(counter)

