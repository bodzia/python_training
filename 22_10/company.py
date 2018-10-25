from employee import Employee

emp1 = Employee('john smith', 'asshole', 14300)
emp2 = Employee('john smith junior', 'not yet asshole', 4300)
#emp2.annual_increase = 0.1

Employee.set_salary(0.6)
print(emp1.position)
print(emp1.annual_increase)
print(emp2.annual_increase)
print(Employee.number_of_employees)
del emp1
print(Employee.number_of_employees)

#if DOB ok
    #create employee

correct_dob = Employee.check_dob('12345678')
print(correct_dob)