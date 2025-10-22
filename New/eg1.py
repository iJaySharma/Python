print("Hello world!")

"""
class Bulb: 
   def __init__(self):
      self.w=0
   def __setattr__(self,name,value):
      print("setattr got called with ",name,value)
   def __getattr__(self,name):
      print("getattr got called with ",name)
   def __getattribute__(self,name):
      print("getattribute got called")
      return 50
b=Bulb()
print(b.w)
b.w=60
print(b.w)
print("*******************************************************************")
#this concept tells whenever getattribute is also given only this runs,priority given to it not attr one




#What if you don’t add super() and just do self.attr = value?
class C:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        self.attr = value   # ❌ bad

c = C()
c.y = 30


#This causes infinite recursion, because self.attr = value calls __setattr__ again.


class Bulb: 
   def __init__(self,w=0):
      self.w=w
   def __new__(cls,w=0):
      print("new of Bulb got called")
      k=super().__new__(cls)
      print("Bulb Initiated")
      return k
   def __setattr__(self,name,value):
      print("setattr got called with ",name,value)
      super().__setattr__(name,value)
   def __getattr__(self,name):
      print(f"{name} attribute does not exist")
      return None
   def __getattribute__(self,name):
      print("getattribute got called")
      return super().__getattribute__(name)      
b=Bulb()
x=Bulb(10)
print(x)
print(x.w)
print(b.w)
print(b.cartoon)
print("***********************************************************************")
#this concept tells about super keyword used in set attr and get attribute methods respectively in such case it runs the property discriptor setter in base class and the get attr method if without return type return None Here does not exists 


c = Bulb(10)
print(c)
d = Bulb(20)


"""

class Bulb: 
   def __init__(self,w=0):
      self.w=w
   def __new__(cls):
      print("new of Bulb got called")
      k=super().__new__(cls)
      print("Bulb Initiated")
      return k
   def __setattr__(self,name,value):
      print("setattr got called with ",name,value)
      super().__setattr__(name,value)
   def __getattr__(self,name):
      print(f"{name} attribute does not exist")
      return None
   def __getattribute__(self,name):
      print("getattribute got called")
      return super().__getattribute__(name)      
b=Bulb()
print(b)
c=Bulb()
print(c)



