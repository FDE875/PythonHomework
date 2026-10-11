
def convert_cel_to_far(C):
   return C * 9/5 + 32
  
   
def convert_far_to_cel(F):
    return (F - 32) * 5/9
F=float(input("Enter a temperature in degrees F: "))
C= convert_far_to_cel(F)

print(f"{F:g} degrees F = {C:.2f}degrees C")
print()

C=float(input("Enter a temperature in degrees C: "))
F= convert_cel_to_far(C)
print(f"{C:g} degrees C= {F:.2f} degrees F")
