a=[2,3,4,3,5,6,7,8]
b=[]
c=2
for i in range ( 0 , len(a), c):
    b.append(a[i:i+c])
print(b)

