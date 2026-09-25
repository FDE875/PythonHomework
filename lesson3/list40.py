a=[1,2,3,4,4,5,4,6,4,7,4,8,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
print(a)