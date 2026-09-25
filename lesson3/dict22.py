a={"c":4,"a":3,"d":6,"b":1,"c":3,}
b={}
for key , value in a.items():
    if 1<value<5:
        b[key]=value
print(b)