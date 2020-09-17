list1 = [1,2,3,4]
with open ('data.txt','w') as f:
    for i in list1:
        i = str(i)
        f.write(i)