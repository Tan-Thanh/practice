import re
class Employee:
    list_info = []
    "Gathering Employee's Information"
    def __init__(self, name, gender, DoB, salary):
        self.name = name
        self.gender = gender
        self.DoB = DoB
        self.salary = salary

    def emp_str_line(self):
        return ('%s    %s    %s    %s' %(self.name, self.gender,self.DoB,self.salary))
    @staticmethod
    def validName():
        while True:
            name = input ('name: ')
            if re.match(r'^[a-zA-Z\s]+$', name) != None:
                break
            else:
                print ("Please enter word character: ")
        return name

    @staticmethod
    def validGender():
        while True:
            gender = input ('gender: ')
            if gender in ['male', 'm', 'M', "Female", "female", 'f']:
                if gender in ['male','m','M']:
                    gender = 'Male'
                    break
                else:
                    gender = 'Female'
                    break
            else:
                print ("Please enter [m-Male] or [f-Female]")
        return gender

    @staticmethod
    def validDoB():
        while True:
            DoB = input ('DoB: ')
            if re.match(r'\d\d\/\d\d\/(19[6-9][0-9]|200[0-2])*$',DoB) != None:
                a = DoB
                if re.match(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)? \d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$',a) != None:
                    break
                else:
                    print ("Please try again *dd/mm/yyyy* ")
            else:
                print ("Please try again *dd/mm/yyyy* ")
                continue
        return DoB

    @staticmethod
    def validSalary():
        while True:
            salary = input ('Salary: ')
            if re.match(r'^[0-9]+$',salary) != None:
                break
            else:
                print ("Please input the number only")
                continue
        return salary
class Manage(Employee):

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
        # print (Employee.list_info)
        return 

    @staticmethod
    def add():
        with open ('data.txt', 'a+') as f:
            name = Employee.validName()
            gender = Employee.validGender()
            DoB = Employee.validDoB()
            salary = Employee.validSalary()
            emp = Employee(name, gender, DoB, salary)
            f.write('\n%s' %Employee.emp_str_line(emp))
            print ('Employee {} was added successfully!'.format(emp.name))
        return 

    @staticmethod
    def edit():
        Manage.view_list_emp()
        list_to_edit = []
        for emp in Employee.list_info:
            emp = emp.rstrip()
            em_parse = emp.split('    ')
            list_to_edit.append(em_parse)
        while True:
            choose_line = int(input ("Which line you want to edit?: "))
            if choose_line in range(1,len(list_to_edit)+1):
                for i in range(len(list_to_edit)):
                    if choose_line == i+1:
                        line_edit = list_to_edit[i]
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
                                print ("Please choose the field 'name', 'gender', 'DoB', 'salary': ")
                                continue
                            list_to_edit[i] = line_edit
                break
            else:
                print ("Please try again!")
                continue
       
        fopen_to_save = open (r'data.txt','w')
        for i in list_to_edit:
            part = '    '.join([str(elem) for elem in i])
            if i == list_to_edit[-1]:
                emp_str_form = ('{}'.format(part))
            else:
                emp_str_form = ('{}\n'.format(part))
            fopen_to_save.write(emp_str_form)
        fopen_to_save.close()
        print ('{} has edited successfully'.format(change_field))
        return
        
    @staticmethod
    def remove():
        Manage.view_list_emp()
        while True:
            choose_line = int(input("Which line do you want to remove?: "))
            if choose_line in range(1,len(Employee.list_info)+1):
                right_choose_line = choose_line
                emp_removed = Employee.list_info.pop(right_choose_line-1)
                print ("{} has been removed!!!".format(emp_removed))
                break
            else:
                print ("Please choose line from 1 to %i." %(len(Employee.list_info)))
        with open('data.txt','w+') as f:
            for emp in Employee.list_info:
                if emp != Employee.list_info[-1]:
                    f.write(emp)
                    f.write('\n')
                else:
                    f.write(emp)

    @staticmethod
    def search():
        Manage.view_list_emp()
        count = 0
        # with open (r'data.txt') as file:
        #     lines = file.readlines()
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
                for emp in Employee.list_info:
                    if choose_gender in emp:
                        count += 1
                        print ('{}. {}'.format(count,emp))
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
                for emp in Employee.list_info:
                    if re.search(r'Male', emp) != None:
                        xxx = 'Male'
                        endpoint = emp.find(xxx)
                    else:
                        xxx = 'Female'
                        endpoint = emp.find(xxx)
                    name_check = emp[0:(endpoint-4)]
                    if choose_name in name_check:
                        count +=1
                        flag = True
                        print ('{}. {}'.format(count,emp))
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
                for emp in Employee.list_info:                    
                    begin_point = emp.find('/')
                    end_point = emp.rfind('/')
                    check_DoB = emp[(begin_point-2) : (end_point+5)]
                    if choose_dob in check_DoB:
                        count +=1
                        flag = True
                        print ('{}. {}'.format(count,emp))
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

                flag = False
                for emp in Employee.list_info:
                    begin_point = emp.rfind(' ')
                    salary_parse = emp[(begin_point+1):len(emp)]
                    if type_search == 'greater':
                        if int(salary_parse) >= value:
                            count +=1
                            flag=True
                            print ('{}. {}'.format(count,emp))
                    elif type_search == 'less':
                        if int(salary_parse) <= value:
                            count += 1
                            flag=True
                            print ('{}. {}'.format(count,emp))

                if not flag:
                    print ("Not Found")
                break
            else:
                continue

        
            
