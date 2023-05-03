def sam(p,q):
    return p,q
print(type(sam))
a=sam
print(type(a))
a(p=10,q=20)
print(a==sam)
a,b=sam(15,25)
print(a,b)

def sam(p,q,r=0):
 return p+q+r
def sam(p,q=0,r=0):
# def sam(p,r=0,q): this is wrong 
 return p+q+r
x=sam(10,20,30)
y=sam(10,2)
z=sam(5)
print(x,y,z)

def doSomething (k):
 k()
def workA():
 print("Great")
def workB():
 print("Cool")
def xyz():
 print("Cannot understand")
x=input("Enter something")
print(f"you have feeded ({x})")
if len(x)>0 and x in "AIJ": doSomething (workA)
elif len(x)>0 and x in "BKC": doSomething (workB)
else: doSomething (xyz)

print("" in "ABCD")

def sam(*x):
 print(f"Number of arguments arrived {len(x)}")
 sum=0
 for i in x: sum+=i
 return sum
print(sam(10,20,30))
print(sam(40,30,40,50,60,70))


def sam(**x):
   print(x,type(x))
sam(a=10,b=20)
sam(Ujjain=[734,233],Indore=(99,55),Bhopal=755)










