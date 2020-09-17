# nếu ta viết 1 method để update email trong class như def thông thường
# thì các object khác sẽ bị ảnh hưởng -> Java họ sẽ dùng getters, setter -> python nó có property decorators
#property decorators cho phép tạo 1 method ta có thể access như 1 attribute -> có nghĩa là obj.attribute -> reuslt
#thay vì method thì là obj.method() (viết thêm parenthesises)
# -> dùng property decorator là @property
# nhưng, nếu method fullname -> attribute thì khi đổi emp_1.fullname = other value
# -> print sẽ báo lỗi: AttributeError: can't set attribute
# -> viết 1 decorator khác (setter)
# deleter: 
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'  #remove!
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    @property #biến fullname từ method -> attribute 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):  #name là value mình muốn đổi, thì nó sẽ đổi luôn first và last -> gọi là setter
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter         #deleter cái attribute -> dùng del emp_1.fullname
    def fullname(self):  
        print ('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('Thanh', "Nguyen")
# emp_1.first = 'AAAA'
emp_1.fullname = 'Thu Le'    #sau khi viết đc 1 setter

print(emp_1.first)
# print (emp_1.email())    #nhưng vậy thì instance nào trong class này đều cũng phải đổi code .email -> .email()
# print (emp_1.fullname()) #nếu đổi emp_1.first = giá trị khác -> email ko đổi??? vì nó tham chiếu tới giá trị
                        #email lấy giá trị first, last ban đầu, self.first thì đã thay đổi
print (emp_1.email)        #đã access lại như 1 attribute            
print (emp_1.fullname)

del emp_1.fullname
print (emp_1.email)