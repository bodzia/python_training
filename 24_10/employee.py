class Employee(object):
    def __init__(self, name, position, ID):
        self.name = name
        self.position = position
        self.__salary = None
        #self._set_salary()
        self.__ID = ID

@property
def salary(self):
    if self.__salary is None:
        return 0
    else:
        return self._salary
@salary.setter
def salary(self,value):
    if isinstance(value,int):
        self.__salary = value

@property
def ID(self):
    if len(self.__ID) == 4:
        return True
    return False

if __name__ == '__main__':
    emp1 = Employee('johnny', 'kalesony', 1234)

    #emp1.salary = 3000
    print(emp1.salary)


#
#     def _set_salary(self):
#         if self.position == 'director':
#             self._salary = 7000
#         else:
#             self._salary = 5000
#
#     def set_ID(self, ID):
#         if len(ID) == 4:
#             self.__ID = ID
#
#     def __check_ID(self,ID):
#         if len(ID) == 4:
#             return True
#         return False
#
# if __name__ == '__main__':
#     emp1 = Employee('johnny', 'kalesony', 1234)
#     emp1._salary = 3000
#     print(emp1._salary)
#     print(emp1._Employee__ID)
#     print(emp1.__dict__)