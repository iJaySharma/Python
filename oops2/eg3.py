class Rectangle:
  def setLength(self,length):
     self.length=length
  def setBreadth(self,breadth):
     self.breadth=breadth
class Box(Rectangle):
  def setHeight(self,height):
     self.height=height
x=Box()
x.setLength(10)
x.setBreadth(2)
x.setHeight(5)
print("Length",x.length)
print("Breadth",x.breadth)
print("Height",x.height)