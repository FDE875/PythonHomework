a={'a':3,'b':2,'c':1,'d':3}
b=3
c=[]
for key, value in a.items():
    if value==b:
        c.append(key)
print(c)