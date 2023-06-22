def abcd(c):
   def pqr():
       print("Great &",c)
   return pqr;
  
a=abcd("cool")
a()

print("***************************")

def lmnop(p,q):
   def pqr():
      print(p,q)
   return pqr
def abcd(c):
   e=[]
   y=1
   x=1000
   while y<=c:
     m=lmnop(x,y)
     e.append(m)
     x=x+1
     y+=1
   return e

a=abcd(10)
for i in a: i()