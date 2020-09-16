class Employee:
    num_of_emps = 0
    count = 0
    def __init__(self, name, gender, DoB, salary):
        self.name = name
        self.gender = gender
        self.dob = DoB
        self.salary = salary
        Employee.count += 1

    def edit_name(self):
        new_name = input('change name: ')
        self.name = new_name
    @classmethod
    def from_string (cls, emp_list):
        name, gender, DoB, salary = emp_list
        return cls(name, gender, DoB, salary)

list_info = []
fopen_to_edit = open(r'C:\Users\KENSHINPC\Desktop\practice\practice\data.txt')
for line in fopen_to_edit:
    line = line.rstrip()
    line_split = line.split('    ')
    list_info.append(line_split)
fopen_to_edit.close()
print (list_info)
for i in range(len(list_info)):
    emp = Employee.from_string(list_info[i])
print (Employee.count)
    

