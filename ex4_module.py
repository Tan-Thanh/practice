import re
class Employee:
    list_info = []
    "Gathering Employee's Information"
    def __init__(self, name, gender, DoB, salary):
        self.name = name
        self.gender = gender
        self.DoB = DoB
        self.salary = salary
        self.emp_str_line = ('%s    %s    %s    %s' %(self.name, self.gender,self.DoB,self.salary))
    # def __str__(self):
    #     return f"{self.name}\t{self.gender}\t{self.DoB}\t{self.salary}"
    @classmethod
    def validName(cls):
        while True:
            cls.name = input ('name: ')
            if re.match(r'^[a-zA-Z\s]+$',cls.name)!=None:
                break
        return cls.name
    @classmethod
    def validGender(cls):
        while True:
            cls.gender = input ('gender: ')
            if cls.gender =='Male' or cls.gender =='Female':
                break
        return cls.gender
    @classmethod
    def validDoB(cls):
        while True:
            cls.DoB = input ('DoB: ')
            if re.match(r'\d\d\/\d\d\/(19[6-9][0-9]|200[0-2])*$',cls.DoB) != None:
                a = cls.DoB
                if re.match(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)? \d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$',a) != None:
                    break
                else:
                    print ("Please try again *dd/mm/yyyy* ")
            else:
                print ("Please try again *dd/mm/yyyy* ")
                continue
        return cls.DoB
    @classmethod
    def validSalary(cls):
        while True:
            cls.salary = input ('Salary: ')
            if re.match(r'^[0-9]*$',cls.salary) != None:
                break
            else:
                print ("Please input the number only")
                continue
        return cls.salary

    def write_out(self):
        foutput = open(r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt', 'a+')
        foutput.write('\n%s' %self.emp_str_line)
        foutput.close()
        print ('Saved!')
        return self
        
    @classmethod
    def view_list_emp(cls):
        cls.fopen = open(r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt')
        cls.count = 0
        print("***************LIST OF EMPLOYEES***************")
        for line in cls.fopen:
            cls.count += 1
            line = line.rstrip()
            print ('{}. {}'.format(cls.count,line))
        cls.fopen.close()
        return 

    @classmethod
    def from_str(cls, str_emp):
        name, gender, DoB, salary = str_emp.split("-")
        return cls(name, gender, DoB, salary)

    @classmethod
    def add(cls):
        name = cls.validName()
        gender = cls.validGender()
        DoB = cls.validDoB()
        salary = cls.validSalary()
        
        return cls(name, gender, DoB, salary)
    @classmethod
    def edit(cls):
        cls.view_list_emp()
        cls.fopen_to_edit = open(r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt')
        for line in cls.fopen_to_edit:
            line = line.rstrip()
            cls.line_split = line.split('    ')
            cls.list_info.append(cls.line_split)
        cls.fopen_to_edit.close()
        while True:
            choose_line = int(input ("Which line you want to edit?: "))
            if choose_line in range(len(cls.list_info)+1):
                for i in range(len(cls.list_info)):
                    if choose_line == i+1:
                        line_edit = cls.list_info[i]
                        while True:
                            change_field = input ("choose the field you want to edit: ")
                            if change_field == 'name':
                                new_name = Employee.validName()
                                line_edit[0] = new_name
                                break
                            elif change_field == 'gender':
                                new_gender = Employee.validGender()
                                line_edit[1] = new_gender
                                break
                            elif change_field == 'DoB':
                                new_DoB = Employee.validDoB()
                                line_edit[2] = new_DoB
                                break
                            elif change_field == 'salary':
                                new_salary = Employee.validSalary()
                                line_edit[3] = new_salary
                                break
                            else:
                                continue
                            cls.list_info[i] = line_edit
                break
            else:
                print ("Please try again!")
                continue
       
        cls.fopen_to_save = open (r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt','w')
        for i in cls.list_info:
            cls.part = '    '.join([str(elem) for elem in i])
            if i == cls.list_info[-1]:
                cls.emp_str_form = ('{}'.format(cls.part))
            else:
                cls.emp_str_form = ('{}\n'.format(cls.part))
            cls.fopen_to_save.write(cls.emp_str_form)
        cls.fopen_to_save.close()
        print ('{} has edited successfully'.format(change_field))
        return

    @classmethod
    def remove(cls):
        cls.view_list_emp()
        with open (r"G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt", "r") as file:
            lines = file.readlines()
        while True:
            choose_line = int(input("Which line do you want to remove?: "))
            if choose_line in range(len(lines)+1):
                right_choose_line = choose_line
                if right_choose_line == (lines.index(lines[-1])+1):
                    lines[-2]=lines[-2].strip('\n')
                break
            else:
                print ("Please choose line from 1 to %i." %(len(lines)))
                continue
        with open(r"G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt", "w") as file:
            for line in lines:
                if line != lines[(right_choose_line-1)]:
                    file.write(line)


        
            
