#CLASS METHOD V.S REGULAR METHOD V.S STATIC METHOD##############
#1. Regular method -> method trong class mà truyền instance vào first arugument (self)
#2. classmethod -> method trong class truyền class vào first argument called CLS
#3. static method -> ko truyền instance hay class vào argument
                # -> hoạt động như regular function ngoại trừ việc nó đặt trong class
                # -> vì có logical connection nào đó với class
class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        
        Employee.num_of_emps += 1
    
    def fullname (self):    #regular methods -> nó auto pass instance vào first arugment mà ta gọi là self
        return "{} {}".format(self.first, self.last)
    
    def apply_raise (self):
         self.pay = int(self.pay * self.raise_amt)

    @classmethod    # a decorator
    def set_raise_amt(cls, amount):  #class method chỉ làm việc với class
        cls.raise_amt = amount       #dùng để thay đổi class varibale

    @classmethod
    def from_string (cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last, pay)     #câu lệnh cls(first, last, pay) cơ bản đã tạo object
                                        #nhưng để nó cho ra kết quả khi gọi method thì dùng "return"

    @staticmethod    # create static method
    def is_workday (day):  #vì nó ko truyền instance hay class nên ko cần self hay cls
        if day.weekday() == 5 or day.weekday() == 6:   # mà chỉ truyền cái mình cần work with
            return False
        return True 


##############################
#class method cung cấp thêm 1 cách khai báo instance
#ví dụ phải parse 1 string rồi mới khai báo object -> dùng class method hiệu quả hơn
#vì data ko phải lúc nào cũng hand typing mà là import từ nhiều sources

emp_str_1 = 'Thanh-Nguyen-12345678'
emp_str_2 = "Thu-Le-87654321"
new_emp_1 = Employee.from_string(emp_str_1)

# first, last, pay = emp_str_1.split('-')    #khai báo biến từ list (assign multiple variables)
# new_emp_1 = Employee(first,last, pay)      #nếu phải parse từng str cực -> classmethod
print (new_emp_1)
print (new_emp_1.email)
print (new_emp_1.pay)
###################################
#Ví dụ viết 1 static method về kiểm tra ngày workday
#-> nó là static vì nó ko liên quan gì instance cụ thể nào hoặc class variable nào
# import datetime
# my_date = datetime.date(2020, 9, 15)
# print (Employee.is_workday(my_date))
########################
# emp1 = Employee('Thanh', 'Nguyen', 12345678)
# emp2 = Employee('Thu', 'Le', 87654321)
###########################

#######################
# emp1.raise_amt = 1.05
# Employee.set_raise_amt(1.07)
# emp1.set_raise_amt(1.05)   #chưa thấy ai dùng class method từ instance, 
                           #và nếu run thì nó sẽ đổi class variable 
                           # -> apply cho tất cả các instance -> dễ nhầm lẫn

# print (Employee.raise_amt)
# print (emp1.raise_amt)
# print (emp2.raise_amt)