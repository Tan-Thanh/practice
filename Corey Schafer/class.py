class Employee:

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname (self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Thanh', 'Nguyen', 8000000)
emp_2 = Employee('Le', 'Thu', 12000000)
#########################
# print (emp_1)
# print (emp_2)
# emp_1.first = 'Nguyen'  #instance variables
# emp_1.last = 'Thanh'
# emp_1.email = 'Nguyen.Thanh@gmail.com'
# emp_1.pay = 8000000
###########################
# emp_2.first = 'Le'  #instance variables
# emp_2.last = 'Thu'
# emp_2.email = 'Le.Thu@gmail.com'
# emp_2.pay = 12000000
# print (emp_1.email)
# print (emp_2.email)
# print ("{} {}".format(emp_1.first, emp_1.last)) #manually -> use method (function in class) def fullname
# print (emp_2.fullname())
# print (emp_1.fullname) #method của class
######################
print (emp_1.fullname())          #gọi method từ instance không pass arg vì tự truyền instance vào self
print (Employee.fullname(emp_1))  #gọi method từ class truyền argument là instance vào self
#########################