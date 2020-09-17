class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):  # tạo subcless kế thừa parent Employee
    raise_amt = 1.10  # viết pass để show là subclass này có thể inheritance parent class các method
    # python xem qua subclass có __init__ gì ko? nếu ko nó sẽ lấy từ parent
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)  # ưu tiên dùng hơn khi có nhiều inheritance
        # Employee.__init__(self, first, last, pay)  #có 2 cách để khai báo thêm attribute cho subclass
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Thanh", "Nguyen", 50000, "Python")
dev_2 = Developer("Thu", "Le", 60000, "Java")
mgr_1 = Manager(
    "Francesco", "Totti", 90000, [dev_1, dev_2]
)  # mgr_1 supervise dev_1 -> đặt 'obj' trong list có cùng location memory

# print (mgr_1.email)
# print (mgr_1.employees)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(help(Developer))       #cho biết thứ tự method và attribue mà subclass lấy
# print (dev_1.pay)
# dev_1.apply_raise()
# print (dev_1.pay)
# print (dev_1.pro_lang)
# print (dev_2.pro_lang)
# ############################
# print(isinstance(mgr_1, Employee))        #kiểm tra sự kế thừa của object và subclass
# print(isinstance(mgr_1, Manager))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
####################################
