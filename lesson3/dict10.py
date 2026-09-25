a={"a":2,"b":4,"c":6,"d":8}
b="b"
if b in a:
    print(f"{b}:{a[b]}")
else:
    print("Not exist key")