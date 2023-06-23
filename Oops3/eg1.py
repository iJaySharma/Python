class aaa:
   def __init__(self):
      print("Initialized")
   def sam(self):
      print("I am sam")
   def __del__(self):
      print("HEre we can write some clean up act")

a=aaa()
print("Object created, it has been initialized")
a.sam()
del a
print("All done")
#a.sam()