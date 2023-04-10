
import datetime


def info(func):
	def inner():
		print(datetime.datetime.now())
		func()
	return inner

@info
def printer():
	print("Hello Everyone..!!")

printer()