x=float(input("Enter a numeber : "))
y=float(input("Enter a number : "))
"""
if x>y:
 print(f'{x} is larger')
else:
     print(f"{y} is larger") 
"""
print(f'{x} id larger') if x>y else print(f'{x} is smaller')
larger=x if x>y else y
print(f'{larger} is larger') 