

my_list = [10, "Pen",5, "Pencile",30,"Ball",80, "Bat"]


price_list = []
item_list = []
for ele in my_list:
	if isinstance(ele,int):
		price_list.append(ele)
	elif isinstance(ele,str):
	 	item_list.append(ele)

temp_list = list(zip(price_list,item_list))
print(temp_list)