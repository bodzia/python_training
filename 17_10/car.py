class Car(object):
    def __init__(self,brand,model,strength):
        self.my_brand = brand
        self.my_model = model
        self.my_strength = strength
        #self.my_skill = True

        def apply_skill(self, skill):
            if skill == 'bark':
                print("bark")
            else:
                print("incorrect skill")

        def action(self):
            self.my_skill = False
