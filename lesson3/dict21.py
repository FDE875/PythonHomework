a={"c":3,"a":3,"d":6,"b":1,"c":3,}
b={}
for value in sorted(a,key=a.get):
    b[value]=a[value]
print(b)
 