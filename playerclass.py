class Player:
    #Class Attribute
    is_registered = 1
    def __init__(self,name,gender,age):
        if Player.is_registered:
            # object Attribute
            self.name = name
            self.gender = gender
            self.age = age
        else:
            print("Please Register Player")

    def get_info(self):

        print("Player Details")
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)

    def set_info(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age


player1 = Player('Sukrut Joshi','Male',28)
player1.get_info()
player1.set_info('Sukrut Joshi','Male',29)
player1.get_info()

player2 = Player('Mohini Joshi','Female',28)

print(Player.is_registered)
