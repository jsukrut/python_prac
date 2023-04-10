import datetime

def print_info(func):
    def inner(func):
        print(datetime.datetime.now())
        func()
        return inner()

@print_info
def printer(name):
    print(name)

printer("ABC")