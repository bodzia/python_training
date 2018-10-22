from animal import Animal

#create instance
new_animal = Animal('dog','big', 3)
print(new_animal)
print(new_animal.my_size)

another_animal = Animal('cat','small',10)
print(another_animal.my_type)

new_animal.apply_skill('bark')
another_animal.apply_skill('miau')
new_animal.action()
print(new_animal.my_skill)
another_animal.my_skill = False
print(another_animal.my_skill)