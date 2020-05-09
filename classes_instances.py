

class Employee:

    raise_amount = 1.04 # class variable
    num_of_employees = 0

    def __init__(self, first, last, pay): #constructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    def applyRaise(self):
        self.pay = int(self.pay * Employee.raise_amount)




print(Employee.num_of_employees)
emp_1 = Employee('Zack','Bunch',95000)
emp_2 = Employee('Will','Rochelle',96000)

print(Employee.num_of_employees)
