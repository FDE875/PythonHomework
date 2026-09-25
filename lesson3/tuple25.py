a=(2,4,5,7,8,3,1,2,3,4,5,6,7)
b=()
for i in a:
    if i not in b:
        b+=(i,)
print(b)