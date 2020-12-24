# nếu ta viết 1 method để update email trong class như def thông thường
# thì các object khác sẽ bị ảnh hưởng -> Java họ sẽ dùng getters, setter -> python nó có property decorators
# property decorators cho phép tạo 1 method ta có thể access như 1 attribute -> có nghĩa là obj.attribute -> result
# thay vì method thì là obj.method() (viết thêm parenthesises)
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
        # self.email = first + '.' + last + '@gmail.com'  #remove! viết vầy thì khi đổi first name/ last name của 1 instance thì 
                                                          #email cũng sẽ ko đổi vì nó đc set ngay từ lúc vừa khai báo instance
                                                          #email ở đây là 1 attribute, khi call là self.email = 
    #có thể dùng method để thay đổi email khi first thay đổi nhưng nếu ai đó đang dùng self.email cho những nơi khác
    # thì sẽ phải đổi từ attribute .email thành method .email()
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property  # biến fullname từ method -> attribute
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    # name là value mình muốn đổi, thì nó sẽ đổi luôn first và last -> gọi là setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # deleter cái attribute -> dùng del emp_1.fullname
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


# emp_1 = Employee('Thanh', "Nguyen")
# emp_1.first = 'AAAA'
# emp_1.fullname = 'Thu Le'  # sau khi viết đc 1 setter

# print(emp_1.first)
# print (emp_1.email())    #nhưng vậy thì instance nào trong class này đều cũng phải đổi code .email -> .email()
# print (emp_1.fullname()) #nếu đổi emp_1.first = giá trị khác -> email ko đổi??? vì nó tham chiếu tới giá trị
                           # email lấy giá trị first, last ban đầu, self.first thì đã thay đổi
# print(emp_1.email)  # đã access lại như 1 attribute
# print(emp_1.fullname)
# 
# del emp_1.fullname
# print(emp_1.email)

#Decorator là để trang trí, bao bọc cho hàm được truyền vào, trong python hàm cũng là 1 đối tượng
#Có nhiều cách decorate: truyền tham số và ko truyền tham số, trong trường hợp truyền tham số thì tham số truyền cho hàm bị decorate
#cũng sẽ được dùng cho hàm decorate
def make_subtract_of(n):
    def subtract(x):
        return n - x
    return subtract
if __name__ == "__main__":
    a = make_subtract_of(2)
    b = make_subtract_of(4)
    c = a(b(2))
    print (c)