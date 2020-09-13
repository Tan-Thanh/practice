# emp12 = Employee.add()

# emp2 = Employee.add()
# emp2 = Employee.write_out(emp2)
# print (emp2)
#######################################################
# name = 'Tan Thanh'
# gender = 'Male'
# DoB = '27/02/1992'
# salary = "123456"
# emp_str_line = ('{}\t{}\t{}\t{}'.format(name, gender,DoB,salary))
# print (emp_str_line)
#########################################################
# a = 'Tan Thanh1'
# b = 1
# pattern = re.match(r'^[a-zA-Z\s]+$',a)
# print (pattern)
# if bool(re.match(r'^[a-zA-Z\s]+$',name)):
########################################################
# a = '27/02/1960'

# pattern = re.match(r'\d{2}/\d{2}/[1960-2002]*$',a)
# # pattern = re.match(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$',a)
# print (pattern)
################   Date of Birthday valid######################################
# import re
# while True:
#     DoB = input ('DoB: ')
#     if re.match(r'\d\d\/\d\d\/(19[6-9][0-9]|200[0-2])*$',DoB) != None:
#         a = DoB
#         if re.match(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$',a) != None:
#             break
#     else:
#         print ("Please try again *dd/mm/yyyy* ")
#         continue
# print (a)
# ###################  Edit file  #########################################
# # a = 'Nguyen Van A-Male-20/5/1994-10000000'
# # 'Le Thi B    Female    02/10/2000    8000000'
# # 'Tran C    Male    10/04/1989    35000000'
# # from ex4_module import Employee
# # fopen = open (r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt')

# # count = 0
# # list_info = []

# # for line in fopen:
# #     count += 1
# #     line = line.rstrip()
# #     print ('{}. {}'.format(count, line))
# #     line_split = line.split('    ')
# #     list_info.append(line_split)

# # print (list_info)
# # # print (list_info[0])
# # # print (list_info[1])
# # # print (list_info[2])
# # fopen.close()
# # while True:
# #     choose_line = int(input ("Which line you want to edit?: "))
# #     if choose_line in range(len(list_info)):
# #         for i in range(len(list_info)):
# #             if choose_line == i+1:
# #                 line_edit = list_info[i]
# #                 while True:
# #                     change_field = input ("choose the field you want to edit: ")
# #                     if change_field == 'name':
# #                         new_name = Employee.validName()
# #                         line_edit[0] = new_name
# #                         break
# #                         # print (line_edit)
# #                     elif change_field == 'gender':
# #                         new_gender = Employee.validGender()
# #                         line_edit[1] = new_gender
# #                         break
# #                     elif change_field == 'DoB':
# #                         new_DoB = Employee.validDoB()
# #                         line_edit[2] = new_DoB
# #                         break
# #                     elif change_field == 'salary':
# #                         new_salary = Employee.validSalary()
# #                         line_edit[3] = new_salary
# #                         break
# #                     else:
# #                         continue
# #                     list_info[i] = line_edit
# #         break
# #     else:
# #         print ("Please try again!")
# #         continue
        
#         # break
# # print (line_edit)
# # print (list_info)
# fopen_to_edit = open (r'G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt','w')
# for i in list_info:
#     part = '    '.join([str(elem) for elem in i])
#     emp_str_form = ('{}\n'.format(part))
#     # print (part)
#     # print (emp_str_form)
#     fopen_to_edit.write(emp_str_form)
# fopen.close()
# fopen_to_edit.close()
# fopen_to_write.close()
#     new_emp = Employee.from_str(part)
#     new_emp = Employee.write_out(new_emp)
#     # for elem in each_map:
#         emp_str = '-'.join(elem))
#         print (emp_str)
#     emp_str_convert = Employee.from_str(emp_str)
#         fopen.write(emp_str)

#############################################


    

# print (line_edit)
# list_info[1] = line_edit
# print (list_info)



# else:
#     while True:
#         choose_line = input ("Which line you want to edit?: ")
#         for line in fopen:
#             count += 1
#             if choose_line = 
#         if choose_line == '1':
#             while True:
#                 field = input ("which field you want to edit [name][gender][DoB][Salary]? ")
#                 if field == 'name':
#                     new_name = input ("What is new name?: ")
#                     pass
# #########Tạo instance = method trong class#############
# import re
# class Employee:
#     "Gathering Employee's Information"
#     def __init__(self, name, gender, DoB, salary):
#         self.name = name
#         self.gender = gender
#         self.DoB = DoB
#         self.salary = salary
#         self.emp_str_line = ('{}\t{}\t{}\t{}'.format(self.name, self.gender,self.DoB,self.salary))
#     @classmethod
#     def from_string (cls, str_line):
#         name, gender, DoB, salary = str_line.split()
#         return cls(name,gender, DoB, salary)
# new_emp = Employee.from_string(abc)
# print (new_emp.name)
# ###########Cách split và join######################
# import re
# a = "Nguyen Van A B    Male    20/5/1994    100000"
# b = 'Tran C    Male    10/04/1989    35000000'
# c = 'Le Thi B    Female    02/10/2000    8000000'

# line_edit = a.split('    ') #4 space
# count = 0
# while True:
#     change_field= input ("choose the field you want to edit: ")
#     if change_field== 'name':
#         new_name = input('new name: ')
#         line_edit[0] = new_name
#         break
#         print (line_edit)
#     elif change_field== 'gender':
#         new_gender = input('new gender: ')
#         line_edit[1] = new_gender
#         break
#     elif change_field== 'DoB':
#         new_DoB = input ('DoB: ')
#         line_edit[2] = new_DoB
#         break
#     elif change_field== 'salary':
#         new_salary = input ('Salary: ')
#         line_edit[3] = new_salary
#         break
#     else:
#         continue
# a_join = '-'.join(line_edit)
# print (line_edit)
# print (a_join)
# new_emp = Employee.from_string(a_join)
# print (new_emp.name)
# # print (type(abc_split))
#############   REMOVE FUNCTION ###################
with open(r"G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt", "r") as f:
    lines = f.readlines()
    # print (lines)
while True:
    a = int(input("line?"))
    if a in range(len(lines)+1):
        b = a
        if b == lines.
        break
    else:
        print ('Try again')
        continue

with open(r"G:\KENSHIN\2020\TMA Solution\workspace2\ex4\data.txt", "w") as f:
    for line in lines:
        if line != lines[(b-1)]:
            if line != lines[-1]:
                f.write(line)
            else:
                lines[-2].rtrip('\n')
                f.write(line)
################## SEARCH FUNCTION ###########################
