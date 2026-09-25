a=[9,8,7,6,3,2,1]
n=4


b=[]

for  x in a:
    b.extend([x]*n)
print(b)