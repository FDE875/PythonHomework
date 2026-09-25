talabalar_royxati={
    "Talaba1":{'ism':"Aziz","kurs":2},
    "Talaba2":{"ism":"Durdona","kurs":2}}
for value in talabalar_royxati.values():
    if type(value)==dict:
        print("Nested dict exist")
