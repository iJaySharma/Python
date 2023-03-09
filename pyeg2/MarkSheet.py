a=input("Enter marks of Physics (0-100) : ")
try:
   physics = float(a)
   if physics.is_integer()==False: exit()
   else: physics=int(physics)
except:
   print(f"Invalid input {a}")
   exit()
if physics<0 or physics>100:
   print(f"Invalid input {physics}")
   exit()
a=input("Enter marks of Chemistry (0-100) : ")
try:
   chemistry = float(a)
   if chemistry.is_integer()==False: exit()
   else: chemistry=int(chemistry)
except:
   print(f"Invalid input : {a}")
   exit()
if chemistry<0 or chemistry>100:
   print(f"Invalid input {chemistry}")
   exit()
a=input("Enter marks of Math (0-100) : ")
try:
   math = float(a)
   if math.is_integer()==False: exit()
   else: math=int(math)
except:
   print(f"Invalid input : {a}")
   exit()
if math<0 or math>100:
   print(f"Invalid input {math}")
   exit()
a=input("Enter marks of English (0-100) : ")
try:
   english = float(a)
   if english.is_integer()==False: exit()
   else: english=int(english)
except:
   print(f"Invalid input : {a}")
   exit()
if english<0 or english>100:
   print(f"Invalid input {english}")
   exit()
a=input("Enter marks of Hindi (0-100) : ")
try:
   hindi = float(a)
   if hindi.is_integer()==False: exit()
   else: hindi=int(hindi)
except:
   print(f"Invalid input : {a}")
   exit()
if hindi<0 or hindi>100:
   print(f"Invalid input {hindi}")
   exit()
failCount=0
if physics<33: failCount+=1
if chemistry<33: failCount+=1
if math<33: failCount+=1
if english<33: failcount+=1
if hindi<33: failCount+=1
total = physics+chemistry+math+english+hindi
print(f"Total is {total}")
if failCount==0:
   print("Result : Pass")
   percentage=round(total/5)
   print(f"Percentage : {percentage}")
   if percentage>=60: print("First division")
   elif percentage>=45: print("Second division")
   else: print("Third division")
if failCount==1:
   print("Result : Supp")
if failCount>1:
   print("Result : fail") 
if physics>=33 and chemistry>=33 and math>=33 and english>=33 and hindi>=33:
   print("Result : Pass")
elif physics<33 and chemistry>=33 and math>=33 and english>=33 and hindi>=33:
   print("Result : Supplement")
elif physics>=33 and chemistry<33 and math>=33 and english>=33 and hindi>=33:
   print("Result : Supplement")
elif physics>=33 and chemistry>=33 and math<33 and english>=33 and hindi>=33:
   print("Result : Supplement")
elif physics>=33 and chemistry>=33 and math>=33 and english<33 and hindi>=33:
   print("Result : Supplement")
elif physics>=33 and chemistry>=33 and math>=33 and english>=33 and hindi<33:
   print("Result : Supplement")
else :
  print("Result : Fail")