from abc import ABC, abstractmethod

#following class is being created by anil 

class Car(ABC):
   @abstractmethod
   def manual(self):
      pass 

class CarServiceStation():  
   def __init__(self,name):
      self.name = name
   def doService(self,car):
      if isinstance(car,Car)==False : raise TypeError(f"{type(car).__name__} is not of Car type")
      car.manual()
      print(f"Car {type(car).__name__} is being serviced by {self.name}")
      print("Servicing complete")

#following class is being created by sunil

class MarutiAlto(Car):
   def doSomething(self):
      print("Whatever")
   def manual(self):
      print("Some details about MarutiAlto")

s=CarServiceStation("PQR service station")
m=MarutiAlto()
m.doSomething()
s.doService(m)