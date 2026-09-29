a="morning"
b= ""
for i in range(len(a)):
    b+=a[i]
    if (i+1)%3==0 and i !=len(a)-1:
        b+="_"
print(b)
    