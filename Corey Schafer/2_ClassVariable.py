class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):  #run everytime ta create instance trong class -> những hàm count để vào đây
        self.fname = first
        self.lname = last
        self.salary = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emps += 1          #số lượng employee thường ít biến đổi nên ta khai báo từ class.variable

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise (self):
        # self.salary = int(self.salary * 1.04)       #nếu ko tham chiếu cls. thì sẽ báo lỗi ko khao báo biến
        # self.salary = int(self.salary * Employee.raise_amount)
        self.salary = int(self.salary * self.raise_amount)  #why? -> nên dùng self vì tùy biến đc theo instance (nếu cần) và subclass có thể override đc
print (Employee.num_of_emps)    #kiểm tra num_of_emps trước khi khai báo instance
emp1 = Employee('Thanh', 'Nguyen', 123456)
emp2 = Employee('Thu', 'Le', 87654321)
#ví dụ kiểu dữ liệu tăng lương hàng nằm cho nhân viên
#ta có thể viết def 1 method tăng amout
# print (emp1.salary) #nếu khoảng rate này thay đổi hàng nằm thì phải chỉnh lại thì mất thời gian
# emp1.apply_raise()  #ta dùng Class variable để nó apply cho tất cả instance trong class
# print (emp1.salary)
# Employee.raise_amount = 1.05   #Nếu change Class variables -> apply cho tất cả instance access tới
# emp1.raise_amount = 1.05         #Nếu khai báo vầy, là khai báo variable riêng cho instance emp1
# print (emp1.__dict__)            #kiểm tra namespace sẽ thấy nó add thêm biến raise_amount vào cho emp1

# print (Employee.raise_amount)
# print (emp1.raise_amount)    #Python sẽ tìm variable trong instance -> ko có sẽ tìm tiếp tới trong class
# print (emp2.raise_amount)    #Class mà instance đc khai báo vào bên trong


# print (emp1.__dict__)        #Dùng để print ra variable và value của instance emp1 -> emp1 ko có variable "raise_amount"
# print (Employee.__dict__)      #Class Emloyee có variable "raise_amount"
########### num_of_emp ################
print (Employee.num_of_emps)
