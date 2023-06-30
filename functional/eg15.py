# partial function example

def aaa(p,q,r):
   print("Inside aaa")
   print(p,q,r)

def pqr(*a):
   print(a)
   print(*a)
   aaa(*a)

print(10,20,30)

def abcd(a,b,c,d):
   return a+b+c+d
 
def partial(func,*a):
   def fff(*b):
      alist=list(a)
      blist=list(b)
      clist=alist+blist
      return func(*clist)
   return fff

one=partial(abcd,10)
two=partial(abcd,10,20)
three=partial(abcd,10,20,30)
print(one(100,200,300))
print(two(1000,2000))
print(three(3333))

@something 
def abcd(a,b,c,d):
   return a+b+c+d

one=abcd(10)
print(one(100,200,300))
two=abcd(10,20)
print(two(1000,2000))
three=abcd(10,20,30)
print(abcd(3333))