a={"ism":"Shaxnoza",
   "familya":"Sattorova",
   "yo`nalish":"Menejment",
   "kurs": 2}
b={"ism":"Doston",
   "familya":"Azizov",
   "yo`nalish":"Matematika",
   "kurs": 1}
for key in a:
    if key in b:
        print("Common key exists")
    else:
        print("Not exists")