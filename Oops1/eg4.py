class aaa:
   x=10
   def sam(k,e):
     k.u=e
   def tom(k):
     print(k.u)
a=aaa()
b=aaa()
print(a.x)
print(b.x)
print(aaa.x)
a.sam(32)
a.tom()
b.sam(64)
b.tom()
print(a.x)
print(b.x)
aaa.x=46
print(aaa.x)
print(a.x)
print(b.x)