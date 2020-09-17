# -*- coding: utf-8 -*-
import re
from ex4_module2 import *
opt = None
print("**********TMA Solutions-Mini Tool**************")
while opt != 'q':
    opt = input('Please choose the function [a-Add, e-Edit, r-Remove, s-Search, v-View, q-Quit]\n')
    if opt == 'a':
        Manage.add()

    elif opt == 'e':
        Manage.edit()

    elif opt == 'r':
        Manage.remove()
    elif opt == 's':
        Manage.search()
    elif opt == 'v':
        Manage.view_list_emp()
    elif opt == 'q':
        break
    else:
        print ('Please chsoose the function or Press "q" to exit program')
        


        