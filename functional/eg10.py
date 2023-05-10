# Collable Objects
class aaa:
   def __init__(self):
      print("init got called")
   def __call__(self,x,y):
      print(x,y)
a=aaa()
a(10,30)

print("***************************************************")

# just example not of collable context
def lmn():
   def pqr():
      print("cool feature")
   print("lmn got called")
   return pqr

b=lmn()
b()

print("********************************************************")

def addHeader(rf):
  def withHeader():
     print("Some cool header")
     rf()
  return withHeader
 
def printReport():
   print("Some financial data")

a=addHeader(printReport)
a()

print("***********************************************************")

def addHeader(rf):
  def withHeader():
     print("Some cool header")
     rf()
  return withHeader

def addFooter(rf):
  def withFooter():
     rf()
     print("Some cool footer")
  return withFooter
 
def printReport():
   print("Some financial data")

a=addFooter(addHeader(printReport))
a()

print("*************************************************************")

def addHeader(rf):
  def withHeader():
     print("Some cool header")
     rf()
  print("addHeader got called")
  return withHeader

def addFooter(rf):
  def withFooter():
     rf()
     print("Some cool footer")
     print("addFooter got called")
  return withFooter
 
@addFooter # second
@addHeader # first
def printReport1():
   print("Some financial data")

printReport1()

@addHeader # thats why second stack is suppose to be maintained thats whyFooter called first
@addFooter # last in first out 
def printReport2():
   print("Some financial data")

printReport2()

print("**********************************************")

def addPercentage(fn):
   def withPercentage(p,c,m,e,h):
      fn(p,c,m,e,h)
      print("Percentage : ",(p+c+m+e+h)//5)
   return withPercentage
 
def addDivision(fn):
   def withDivision(p,c,m,e,h):
      fn(p,c,m,e,h)
      per=(p+c+m+e+h)//5
      if per>=60:
          print("First division")
      elif per>=45:
          print("Second division ")
      else:
          print("Third division")
   return withDivision 

@addDivision
@addPercentage
def processResult(p,c,m,e,h):
   print("Total : ",p+c+m+e+h)

processResult(50,40,50,60,70)


































