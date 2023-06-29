# partial function 
import functools as ft
import inspect as inspector
def add(a,b):
   return a+b
 
def addToX(x):
   def fff(y):
      return add(x,y)
   return fff

addTo10=addToX(10)
print(addTo10(20))
print(addTo10(30))

b=[100,200,30,50,40,20]
c=list(map(addToX(10),b))
print(c)

def add(a,b):
   return a+b
 
addTo10=ft.partial(add,10)
print(addTo10(20))

def abcd(a,b,c,d,k,f,dd,s,g):
   pass

s=inspector.signature(abcd)
print(type(s))
print(s.parameters)
print(len(s.parameters))