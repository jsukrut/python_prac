def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :

myFun('geeks', 'for', 'geeks', first=[1,2,3,4,5], mid="for", last="Geeks")


