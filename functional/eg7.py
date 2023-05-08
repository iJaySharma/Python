def xyz():
   x=1
   yield x
   x+= 1
   yield x
   x+=1
   yield x
a=xyz()
print(type(a))
for i in a: print(i)

x=[10,13,20,40,21,43,7]
b=(i for i in x)
print(type(b))
c=list(b)
print(c)