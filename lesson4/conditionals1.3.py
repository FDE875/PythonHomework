list1=[1,1,2,3,4,2]
list2=[1,3,4,5]
a=[]
for i in list1:
    if i not in list2:
        a.append(i)
for i in list2:
    if i not in list1:
        a.append(i)
        print(a)
