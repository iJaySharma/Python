class aaa:
   def __init__(self,x):
      self.x = x
      print("aaa initialized  with ",x)

class bbb(aaa):
   def __init__(self,x,y,z):
      super().__init__(x,z)
      self.y=y
      print("bbb initialized with ",y)
   def __str__(self): 
      return f"{self.x},{self.y}"
 
class ccc(aaa):
   def __init__(self,x,z):
      super().__init__(x)
      self.z=z
      print("ccc initialized with ",z)
   def __str__(self):
      return f"{self.x},{self.z}"

class ddd(bbb,ccc):
   def __init__(self,x,y,z,k):
      super().__init__(x,y,z)
      self.k=k
      print("ddd initialized with ",k)
   def __str__(self):
      return f"{self.x},{self.y},{self.z},{self.k}"

d=ddd(1000,2000,3000,4000)
print(d)