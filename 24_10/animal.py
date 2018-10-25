class Animal(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'animal {self.name} moved.')

class Horse(Animal):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)

    def move(self):
        print(f'horse {self.name} run.')

    def jump(self, how_high):
        if how_high > 5:
            print(f'horse {self.name} jumped high.')
        else:
            print(f'horse {self.name} jumped low.')

class Donkey(Animal):
    #def __init__(self, stubborn, owner, hungry):
    def __init__(self, stubborn):
        #self.owner = owner
        #self.hungry = hungry
        self.stubborn = stubborn
        super().__init__('unknown')

    def move(self):
        if self.stubborn > 8:
            print(f'donkey is stubborn, won\'t move.')
        else:
            print(f'donkey moved a bit.')

class Mule(Horse, Donkey):
    def __init__(self, name, color):
        super().__init__(name,color)

if __name__ == '__main__':
    #print(help(Mule))
    #print(Mule.mro())
    #print(Mule.__mro__) mro - method resolution order


    e_mule = Mule('johnny', 'black')
    print(e_mule.name)
    e_mule.move()