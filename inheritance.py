
class Employee:

    raise_amount = 1.04 # class variable


    def __init__(self, first, last, pay): #constructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'



    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)


#developer inherits from Employee
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())





dev_1 = Developer('Corey', 'Shafer',50000,'Python')
dev_2 = Developer('Tom', 'Sawyer',70000, 'Java')
manager_1 = Manager('Josh','Adkins',70000,[dev_1])

print(isinstance(manager_1,Developer))
print(issubclass(Developer,Employee))


# print(manager_1.email)
# manager_1.add_emp(dev_2)
# manager_1.print_emps()
#
#
# # print(help(Developer))
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.applyRaise()
# print(dev_1.pay)
