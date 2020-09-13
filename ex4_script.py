# -*- coding: utf-8 -*-
import re
from ex4_module import Employee
opt = None
print("**********TMA Solutions-Mini Tool**************")
while opt != 'q':
    opt = input('Please choose the function [a-Add, e-Edit, r-Remove, s-Search, v-View]\n')
    if opt == 'a':
        pass
        emp = Employee.add()
        emp = Employee.write_out(emp)
    elif opt == 'e':
        edit = Employee.edit()
    elif opt == 'r':
        remove = Employee.remove()
    elif opt == 's':
        pass
    elif opt == 'v':
        Employee.view_list_emp()
    elif opt == 'q':
        break
    else:
        print ('Please chsoose the function or Press "q" to exit program')
        


        