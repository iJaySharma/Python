def string_length(s):
   print("string_length: got called with argument ",s)
   return len(s)
def int_length(i):
   print("int_length: got called with argument ",i)
   return string_length(str(i))

def get_length_of_elements(t):
   a= []
   for i in t:
      if isinstance(i,int): a.append(int_length)
      if isinstance(i,str): a.append(string_length)
   return length_of_elements_iterator_factory(t,a)

class length_of_elements_iterator_factory:
   def __init__(self,t,a):
      self.t=t
      self.a=a 
   def __iter__(self):
      return length_of_elements_iterator(self)

class length_of_elements_iterator:
  def __init__(self,obj):
     self.t=obj.t
     self.a=obj.a
     self.index=0
  def __next__(self):
   if self.index>=len(self.t): raise StopIteration
   fn=self.a[self.index]
   k=fn(self.t[self.index])
   self.index+=1
   return k

a=(10,20,"Good","Ujjain is the city of gods",30)
b=get_length_of_elements(a)
print()
print()
print("called length_of_elements")
print()
print()
for i in b: print(i)