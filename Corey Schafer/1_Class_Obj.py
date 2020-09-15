class Employee:
    "This is to introduce Class Employee"  #đoạn __doc__ string giới thiệu về clas
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.salary = pay
        self.email = first + '.' + last +'@gmail.com' #có thể khao báo thêm biến trong def __init__
    
    def fullname (self):
        return '{} {}'.format (self.fname, self.lname)  #dùng print khi executive sẽ trả về theo hàm return


emp1 = Employee("Thanh", "Nguyen",12345678)
emp2 = Employee("Thu", "Le", 87654321)

# print (emp1.fname)
# print (emp1.email)
print (emp1.fullname())  #cách 1 để gọi hàm từ instance ko cần truyền argument self vì nó tự vào
print (Employee.fullname(emp1))  #cach2  gọi hàm từ class.method (thì phải truyền instance vào)
print (emp1.email)

# emp2 = Employee()
# print (emp1.first) #lỗi vì attribute đi theo instace là self.fname, first chỉ là arugment khai báo trong __init__ để truyền vào thôi 
# print (emp1.fname)
# emp1.first = "Thanh"                      #instance variables
# emp1.last = "Nguyen"                      #instance variables
# emp1.email = 'Thanh.Nguyen@gmail.com'     #instance variables
# emp1.pay = 12345678                       #instance variables

# emp2.first = "Thu"
# emp2.last = "Le"
# emp2.email = 'Thu.Le@gmail.com'
# emp2.pay = 87654321


# print (emp1.first) # thay vì phải khai báo từng attribute cho từng instance -> dùng class Employee(self, first, last, pay)
# print (emp2.first) # riêng email thì sẽ viết concatinate first.last@gmail.com

# print (emp1)  #location memory không đổi
# print (emp2)

# print (Employee) #show đc __name__ = __main___ -> script đang thực thi
