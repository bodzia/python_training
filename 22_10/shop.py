from product import Product

p1 = Product('shoes', 'black', 23.00)
p2 = Product('shoes', 'red', 24.00)

print(p1)
print(p2)

shopping = [p1,p2]
print(shopping)

print (p1 == p2)

value =  p1+ p2
print(value)