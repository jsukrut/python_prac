class Infiniteiterator:
    def __init__(self,limit):
        self.limit = limit
        self.val =0

    def __iter__(self):
        self.val = 0
        return self
        
    def __next__(self):
        if self.val < self.limit:
            self.val +=1
            return self.val


obj = Infiniteiterator(100)
# iter_obj = iter(obj)
for i in range(100):
    print(next(obj))

