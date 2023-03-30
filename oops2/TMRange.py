class TMRange:
  def __init__(self,start,end,step=1):
     self.start=start
     self.end=end 
     self.step=step
  def __str__(self):
     return f"TMRange({self.start},{self.end})"
  def __iter__(self):
     iterator=TMRangeIterator(self)
     return iterator
class TMRangeIterator:
  def __init__(self,obj):
     self.start=obj.start
     self.end=obj.end
     self.step=obj.step
     self.current=self.start
  def __next__(self):
     if self.current>self.end: raise StopIteration
     data=self.current 
     self.current+=self.step
     return data
  def __str__(self):
     return f"TMRangeIterator({self.start},{self.end})"
x=TMRange(1,3)
for i in x:
   for j in x:
      for k in x:
         print(i,j,k)