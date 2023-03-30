class Rectangle:
  def __init_(self,length,breadth):
     self.length=length
     self.breadth=breadth
class Box(Rectangle):
  def __init__(self,length,breadth,height):
     super().__init__(length,breadth)
     self.height=height
x=Box(10,2,5)
print("Length",x.length)
print("Breadth",x.breadth)
print("Height",x.height)