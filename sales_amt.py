
from collections import Counter
no_of_shoes = 10
shoes_list = [2, 3, 4, 5,6, 8, 7, 6, 5, 18]
customers = 6
ordres =[(6,55),(6,45),(6 ,55),(4,40),(18, 60),(10, 50)]

availbale_shoes = Counter(shoes_list)

sales_amount = 0
for order in ordres:
	if order[0] in availbale_shoes.keys():
		if availbale_shoes.get(order[0])> 0:
			sales_amount = sales_amount + order[1]
			availbale_shoes[order[0]] = availbale_shoes[order[0]] - 1
		else:
			print("no shoes")

print(sales_amount)















# from collections import Counter
# no_of_shoes = int(input())
# list_of_shoes = map(int,(input().split()))
# customers = int(input())
# ordres = map(tuple,(map(int,input().split()) for _ in range(customers)))
# availbale_shoes = Counter(list_of_shoes)

# sales_amount = 0
# for order in ordres:
#     if order[0] in availbale_shoes.keys():
#         if availbale_shoes.get(order[0])> 0:
#             sales_amount = sales_amount + order[1]
#             availbale_shoes[order[0]] = availbale_shoes[order[0]] - 1
#         # else:
#         #     print("Size {0} no longer available, so no purchase.".format(order[0]))

# print(sales_amount)
    


