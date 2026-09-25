a=(1,2,7,3,8,4,5)
b=(1,6,2,7,8,3,9)
c=[]
for i in a:
    if i not in b:
        c.append(i)

print(tuple(c))