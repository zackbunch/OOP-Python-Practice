

class Employee:
    def __init__(self, first, last, pay): #constructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)





emp_1 = Employee('Zack','Bunch',95000)

print(Employee.fullname(emp_1))
# print(emp_1.fullname())
