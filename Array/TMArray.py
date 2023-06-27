import array as arr
x=arr.array('i')
y=1
while y<=15:
   x.append(0)
   y+=1
rows=5
columns=3
for r in range(rows):
   for c in range(columns):
      x[(r*columns+c)]=int(input(f"Enter value for [{r}][{c}] :"))
y=0
while y<=14:
   print("%10d" % (x[y]),end="") 
   y+=1
   if y%3==0: print()

