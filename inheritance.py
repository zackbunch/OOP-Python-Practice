
class Employee:




    def __init__(self, first, last): #constructor method
        self.first = first
        self.last = last



    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

emp1 = Employee('John','Smith')

emp1.first = 'Jim'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
