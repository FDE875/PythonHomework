a={"a":2,"b":4,"c":5,"d":6}
b={}
for key, value in a.items():
    b[value]=key
print(b)