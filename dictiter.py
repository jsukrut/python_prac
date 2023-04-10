

def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)

nested_dictionary = {"dict1": {"a": {'c':{'d':1}}},"dict2": {"b": 2}}
get_all_values(nested_dictionary)
