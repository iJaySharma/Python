class Bulb:
   def __init__(self,w):  
      self.w = w
   """ def __str__(self):
     return f"Wattage : {self.w}" """
   def __repr__(self):   
      return f"Bulb({self.w})" 
b = Bulb(1000)
#print(b)
#print(b.__str__())
print(b.__repr__())  
c=eval(repr(b))
print(c)

d = "10*5"
print(eval(d))

# By default call goes to repr {string representation of unambiguity in terms of understandibiity of data types and if use with eval kind of function operator used to create object if is in object instantiation form other wise eval be also used as if arithmatic computation}