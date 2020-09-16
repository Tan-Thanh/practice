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

    @classmethod
    def validName(cls):
        while True:
            cls.name = input ('name: ')
            if re.match(r'^[a-zA-Z\s]+$',cls.name)!=None:
                break
            else:
                print ("Please enter word character: ")
        return cls.name

    @classmethod
    def validGender(cls):
        while True:
            cls.gender = input ('gender: ')
            if cls.gender in ['male', 'm', 'M', "Female", "female", 'f']:
                if cls.gender in ['male','m','M']:
                    cls.gender = 'Male'
                    break
                else:
                    cls.gender = 'Female'
                    break
            else:
                print ("Please enter [m-Male] or [f-Female]")
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
            if re.match(r'^[0-9]+$',cls.salary) != None:
                break
            else:
                print ("Please input the number only")
                continue
        return cls.salary

    def write_out(self):
        foutput = open(r'data.txt', 'a+')
        foutput.write('\n%s' %self.emp_str_line)
        foutput.close()
        print ('Employee was added successfully!')
        return self

    @classmethod
    def from_list(cls, emp_list_format):
        name, gender, DoB, salary = emp_list_format
        return cls(name, gender, DoB, salary)

    @staticmethod
    def view_list_emp():
        count = 0
        fopen = open(r'data.txt')
        print("*************** EMPLOYEES LIST ***************")
        print ("No.    Name    Gender    Date of birth    Salary")
        for line in fopen:
            count += 1
            line = line.rstrip()
            print ('{}. {}'.format(count,line))
            if line not in Employee.list_info:
                Employee.list_info.append(line)
            

        fopen.close()
        print ("Number of Employees current: ", count)
        print (Employee.list_info)
        return 

    @classmethod
    def add(cls):
        with open ('data.txt', 'w') as f:
            for emp in Employee.list_info:
                emp_split = emp.split('   ')
                add_emp = Employee.from_list(emp_split)
            add_list = Employee.list_info()
            name = cls.validName()
            gender = cls.validGender()
            DoB = cls.validDoB()
            salary = cls.validSalary()
            emp = Employee(name, gender, DoB, salary)
            if emp not in add_list:
                add_list.append(emp)
            for line in add_list:
                f.write(line)
        return cls(name, gender, DoB, salary)
    # @classmethod
    # def edit(cls):
    #     cls.view_list_emp()
    #     list_to_edit = []
    #     fopen_to_edit = open(r'data.txt')
    #     for line in fopen_to_edit:
    #         line = line.rstrip()
    #         line_split = line.split('    ')
    #         list_to_edit.append(line_split)
    #     fopen_to_edit.close()
    #     while True:
    #         choose_line = int(input ("Which line you want to edit?: "))
    #         if choose_line in range(1,len(list_to_edit)+1):
    #             for i in range(len(list_to_edit)):
    #                 if choose_line == i+1:
    #                     line_edit = list_to_edit[i]
    #                     while True:
    #                         change_field = input ("choose the field you want to edit: ")
    #                         if change_field == 'name':
    #                             new_name = Employee.validName()
    #                             line_edit[0] = new_name
    #                             break
    #                         elif change_field == 'gender':
    #                             new_gender = Employee.validGender()
    #                             line_edit[1] = new_gender
    #                             break
    #                         elif change_field == 'DoB':
    #                             new_DoB = Employee.validDoB()
    #                             line_edit[2] = new_DoB
    #                             break
    #                         elif change_field == 'salary':
    #                             new_salary = Employee.validSalary()
    #                             line_edit[3] = new_salary
    #                             break
    #                         else:
    #                             continue
    #                         list_to_edit[i] = line_edit
    #             break
    #         else:
    #             print ("Please try again!")
    #             continue
       
    #     fopen_to_save = open (r'data.txt','w')
    #     for i in list_to_edit:
    #         part = '    '.join([str(elem) for elem in i])
    #         if i == list_to_edit[-1]:
    #             emp_str_form = ('{}'.format(part))
    #         else:
    #             emp_str_form = ('{}\n'.format(part))
    #         fopen_to_save.write(emp_str_form)
    #     fopen_to_save.close()
    #     print ('{} has edited successfully'.format(change_field))
    #     return
        
    # @classmethod
    # def remove(cls):
    #     Employee.view_list_emp()
    #     with open (r"data.txt", "r") as file:
    #         lines = file.readlines()
    #     while True:
    #         choose_line = int(input("Which line do you want to remove?: "))
    #         if choose_line in range(len(lines)+1):
    #             right_choose_line = choose_line
    #             if right_choose_line == (lines.index(lines[-1])+1):
    #                 lines[-2]=lines[-2].strip('\n')
    #             break
    #         else:
    #             print ("Please choose line from 1 to %i." %(len(lines)))
    #             continue
    #     with open(r"data.txt", "w") as file:
    #         for line in lines:
    #             if line != lines[(right_choose_line-1)]:
    #                 file.write(line)

    @classmethod
    def search(cls):
        cls.view_list_emp()
        cls.count = 0
        with open (r'data.txt') as file:
            lines = file.readlines()
        while True:            
            while True:
                choose_key = input ("Which 'key' do you want to search by?: ")
                if choose_key in ['name', 'gender', 'DoB', 'salary']:
                    break
                else:
                    print ("Please enter the key to search 'name', 'gender', 'DoB', 'salary'")                   
            if choose_key == 'gender':
                while True: 
                    choose_gender = input ("Which gender do you want to search (Male/Female)?: ")
                    if choose_gender == 'Male' or choose_gender == 'Female':
                        break
                    else:
                        print ("Please enter correct gender 'Male' / 'Female'")
                print ("######### SEARCH RESULT BY '{}' - '{}' ! ##########".format(choose_key,choose_gender))
                for line in lines:
                    if choose_gender in line:
                        cls.count += 1
                        print ('{}. {}'.format(cls.count,line.rstrip('\n')))
                else:
                    break

            elif choose_key == 'name':
                while True:
                    choose_name = input ("What name do you want to search?: ")
                    if re.match(r'^[a-zA-Z\s]+$',choose_name) !=None:
                        break
                    else:
                        print ("Please enter a text only")                        
                print ("######### SEARCH RESULT BY '{}' - '{}' ! ##########".format(choose_key,choose_name))
                flag = False
                for line in lines:
                    if re.search(r'Male', line) != None:
                        xxx = 'Male'
                        endpoint = line.find(xxx)
                    else:
                        xxx = 'Female'
                        endpoint = line.find(xxx)
                    name_check = line[0:(endpoint-4)]
                    if choose_name in name_check:
                        cls.count +=1
                        flag = True
                        print ('{}. {}'.format(cls.count,line.rstrip('\n')))
                if not flag:
                    print ("Not Found!")
                break

            elif choose_key == 'DoB':
                while True:
                    choose_dob = input ("What DoB do you want to search?: ")
                    if re.match(r'\d\d|\d\d\/\d\d\|\d\d\/\d\d\/(19[6-9][0-9]|200[0-2])*$',choose_dob) != None:
                        break
                    else:
                        print ("Please enter a correct DoB")
                print ("######### SEARCH RESULT BY '{}' contains number '{}' ! ##########".format(choose_key,choose_dob))
                flag = False
                for line in lines:                    
                    if line != line [-1]:
                        line = line.rstrip('\n')
                    begin_point_num = line.find('/')
                    end_point_num = line.rfind('/')
                    check_DoB = line[(begin_point_num-2) : (end_point_num+5)]
                    if choose_dob in check_DoB:
                        cls.count +=1
                        flag = True
                        print ('{}. {}'.format(cls.count,line.rstrip('\n')))
                if not flag:
                    print ("Not found")
                break

            elif choose_key == 'salary':
                while True:
                    type_search = input ("What kind of searching greater/less than? ")
                    if type_search == 'greater' or type_search == 'less':
                        break
                    else:
                        print ("Please enter the correct kind of searching!") 
                while True:
                    try:
                        value = int(input ("Enter the value {} than: ".format(type_search)))
                    except ValueError:
                        print ("Please enter a correct value - integer: ")
                    else:
                        break
                print ("######### SEARCH RESULT BY '{}' ! ##########".format(choose_key))
                with open (r'data.txt') as file:
                    lines = file.readlines()
                    found=False
                    for line in lines:
                        if line != lines[-1]:
                            line = line.rstrip('\n')
                        begin_point_num = line.rfind(' ')
                        split_salary = line[(begin_point_num+1):len(line)]
                        if type_search == 'greater':
                            if int(split_salary) >= value:
                                cls.count +=1
                                found=True
                                print ('{}. {}'.format(cls.count,line.rstrip('\n')))
                        elif type_search == 'less':
                            if int(split_salary) <= value:
                                cls.count +=1
                                found=True
                                print ('{}. {}'.format(cls.count,line.rstrip('\n')))

                    if not found:
                        print ("Not Found")
                    break
            else:
                continue
        # with open (r'data.txt','w') as file: #recover root list
        #     for line in lines:
        #         file.write(line)
        
            
