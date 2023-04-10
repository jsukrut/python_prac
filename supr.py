
class A:
    def __init__(self):
        print('Initializing: class A')

class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

if __name__ == '__main__':
    c = C()
