class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = first + "." + last + '@gmail.com'
        self.pay = pay
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

emp1 = Employee('Himura', 'KenShin', 50_000)
# print (emp1.fullname())
emp1.last = 'ABC'
print (emp1.fullname)
print (emp1.email)
emp1.fullname = "AAA BBB"
print (emp1.fullname)
print (emp1.email)
