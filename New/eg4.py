from abc import ABC,abstractmethod  # or import abc as ab 

class Vehicle(ABC):  # or ab.ABC
   @abstractmethod # or @ab.abstractmethod
   def manual():
      pass

class Maruti(Vehicle):
   def manual(self):
      print("Maruti")

class Ford(Vehicle):
   def manual():
      ...

class Honda(Vehicle):
   pass

#v = Vehicle()
m = Maruti()
f = Ford()
h = Honda()

m.manual()
f.manual()