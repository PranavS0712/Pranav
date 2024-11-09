class Robot :
    def __init__(self,name) :
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self,x):
        self.position[0] = self.position[0]+x
        print('New Position :', self.position)
    
    def eat(self):
        print('I am hungry')
        

class Robot_Dog(Robot):
    def make_noise(Self):
        print('Woof Woof !')
    
    def fav_food(self):
            print('I eat meat')
            print('--------------')

    def eat(Self):
        super().eat()
        print('I Like bacon !')
    
class Robot_Cat(Robot):
    def make_noise(self):
        print('Meow Meow !')
 
    def fav_food(self):
        print('I eat fish')
        print('--------------')

my_robot_dog = Robot_Dog('Pintu')
my_robot_dog.eat()
