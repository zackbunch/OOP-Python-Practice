

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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Zack','Bunch',95000)
emp_2 = Employee('Will','Rochelle',96000)

# static methods

import datetime
my_date = datetime.date(2020,5,11)

print(Employee.is_workday(my_date))
