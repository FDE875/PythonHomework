import string 
password=str(input(('Enter a password: ')))

if len(password)<8:
    print("Password is too short")
elif not any(c.isupper() for c in password):
    print("Password must contain an uppercase letter")
else:
    print( "Password is strong")
