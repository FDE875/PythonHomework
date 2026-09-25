a={2,3,4,5,6,7,8,9}
b=set()
for i in a:
    if i%2==1:
        b.add(i)
print(b)