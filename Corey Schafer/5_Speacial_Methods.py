#special method cho phép mô phỏng built-in behavior within Python
#và thực hiện nạp chồng toán tử operator overloading
# vd 1+2 = 3 còn a + b =ab -> gọi là behavior nhưng cùng 1 operator là plus
# vd khi print 1 ob nó hiện location memory -> dùng special method để print out
# kết quả nhìn user-friendly hơn <__main__.Employee object at 0x000001AFBB5F7B88>
# 2 special method thường gặp __repr__ và __str__ đùng để print out và display 1 object
# nếu cùng khai báo repr và str khi print object nó ưu tiên str
# muốn print out riêng thì print (repr(emp1)) và print (str(emp1))
# đối với special method khi nó ko apply đc cho các object nhưng 1 số object cần dùng
# ta cho nó return NotImplemented để fallback cho các trường hợp khác dùng
# nếu ko nó sẽ traceback tất cả các trường hợp khác 
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay): #là 1 special method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)
    
    def __repr__(self): #dùng để debugging logging hiển thị mờ ảo
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self): #hiển thị 1 cách có thể đọc đc -> cho end-user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): #self là emp1, other hàm ý chỉ object còn lại
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
emp_1 = Employee('Thanh', 'Nguyen', 50000)
emp_2 = Employee('Thu', 'Le', 60000)
print (emp_1) #<__main__.Employee object at 0x000001AFBB5F7B88> trước khi chưa có __repr__
print (repr(emp_1))
print (str(emp_1))
print (emp_1.__repr__())
print (emp_1.__str__())
print (1+2) #-> print (int.__add__(1,2)) object interger có special method add
print (int.__add__(1,2))
print (str.__add__('a','b')) #-> object string có special method concatenate
#ví dụ muốn tính tổng lương của 2 employ ee = cách add 2 employ -> def lại special method add
print (emp_1 + emp_2)
len cũng là 1 special method của string object
print (len('test'))
print ('test'.__len__())
print (len(emp_1))
