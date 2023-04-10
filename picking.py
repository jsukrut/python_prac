import pickle
my_list = {15, 'Python', 'Hello World'}
# Pickling
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)
with open("data.pickle","rb") as file_handle:
    retrieved_data = pickle.load(file_handle)
    print(retrieved_data)
