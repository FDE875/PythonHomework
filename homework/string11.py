c=input("enter a string: ")

if any(char.isdigit() for char in c ) : print("digit is  in the string" )
else:print("digit is not in the string")