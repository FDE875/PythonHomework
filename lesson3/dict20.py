a={"c":3,"a":3,"d":5,"b":4,"c":3,}
b={}
for key in sorted(a):
    b[key]=a[key]
print(b)
 