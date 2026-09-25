a=(2,4,5,6,7,8,9)
b=2
c=()
for x in a:
    c+=(x,)*b
print(c)