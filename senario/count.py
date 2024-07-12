from collections import Counter

my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
counter = Counter(my_list)
most_common_elements = counter.most_common()
print("-most_common_elements-",most_common_elements)


# fsbjbfjf
counter_dict ={}
my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]

for no in my_list:
    if no in counter_dict.keys():
        counter_dict[no] += 1
    else:
        counter_dict[no] = 1
max_count = max(counter_dict.values())
occ = [(k,v) for k,v in counter_dict.items() if v ==max_count ]
print(counter_dict)
print(occ)

