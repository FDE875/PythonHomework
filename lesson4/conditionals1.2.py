list1=[1,2,3]
list2=[4,5,6]
a=[]
for i in list1:
    if i not in list2:
        a.append(i)
for i in list2:
    if i not in list1:
        a.append(i)
print(a)