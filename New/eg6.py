class GenderDescriptor:
   def __init__(self):
      print("init of Gender Descriptor got called")
      self._attribute_name = "gender"

   def __set__(self,instance,value):
      instance.__dict__[self._attribute_name] = value
      print(f"set method got called for instance of {type(instanc).__name__}")


class Person:
   gender = GenderDescriptor()

   def __init__(self,name,gender):
      self.name = name 
      self.gender = gender

p = Person("alice","Female")




























































































-




















=













] )