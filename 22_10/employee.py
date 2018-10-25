class Employee(object):

    annual_increase = 0.05
    number_of_employees = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.number_of_employees += 1

    @classmethod
    def set_salary(cls, value):
        if cls.annual_increase + value < cls.annual_increase * 1.1:
            cls.annual_increase = value
        else:
            cls.annual_increase = cls.annual_increase * 1.1

    def __del__(self):
        Employee.number_of_employees -=1

    @staticmethod
    def check_dob(dob):
        if len(dob) != 8:
            return False
        return True