# nested comprehension examples
a=[[10,20,30],[533,23,44],[75,67,785,343]]
e=0
while e<len(a):
  f=0
  while f<len(a[e]):
     print(a[e][f])
     f+=1
  e+=1

a=[[10,20,30],[40,55,60],[70,80,90]]
for e in a:
   for f in e:
     if f%2==0: print(f)

print("**************************************")
b=(f for e in a for f in e)
c=list(b)
print(c)