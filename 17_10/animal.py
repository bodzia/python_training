class Animal(object):
    def __init__(self,type,size,age):
        self.my_type = type
        self.my_size = size
        self.my_age = age
        self.my_skill = True

    def apply_skill(self,skill):
        if skill == 'bark':
            print("bark")
        else:
            print("incorrect skill")

    def action(self):
        self.my_skill = False

    def __str__(self):
        return f"animal {self.my_type}, is {self.my_age} old. "