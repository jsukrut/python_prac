dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

# dict uppacking

dict3 ={**dict1,**dict1}
print(dict3)
