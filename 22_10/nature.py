class Nature(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'object {self.name} has moved.')

class HumanBeing(Nature):
    def __init__(self,first_name, age):
        super().__init__(first_name)
        #Nature.__init__(first_name)
        self.first_name = first_name
        self.age = age

    def move(self):
        print(f'{self.name} is walking.')

class Doggy(Nature):
    def __init__(self,name, age, color):
        super().__init__(name)
        self.age = age
        self.color = color

    def bark(self):
        print(f'dog {self.name} is barking')

class Kitty(Nature):
    def __init__(self,name, age, color):
        super().__init__(name)
        self.age = age
        self.color = color

    def miau(self):
        if self.age > 5:
            return True
        else:
            return False

class Student(HumanBeing):
    def __init__(self, name, bla):

