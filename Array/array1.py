import array
a=array.array('i')
a.append(10)
a.append(123124242424442233)
a.append(-30)
a.append(40)
a.append(50)
for x in a: print(x)
print(a[2])
print(a[3])
x=0
while x<=4: 
  print(a[x])
  x=x+1
ep=len(a)-1
x=0
while x<=ep:
   print(a[x])
   x=x+1
print(len(a))
x=range(5)
for i in x: print(i)
for i in x: print(a[i])
print(a.itemsize)
x=123124242424442233