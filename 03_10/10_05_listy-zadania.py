# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
list = [10,20,30,20,10,50,60,40,80,50,40]

number_of_elements = len(list)
i = 0

while i < number_of_elements:

     number_of_occurences = list.count(list[i])
     element = list[i]

     if number_of_occurences > 1:

         if element in list:
             list.remove(element)
         #print("lista po kasacji: ", list)
         number_of_elements=len(list)

     i += 1

print("lista po kasacji: ", list)

# lista = [10,20,30,20,10,50,60,40,80,50,40]
#
# print("test", list(set(lista)))
#[40, 10, 80, 50, 20, 60, 30]
