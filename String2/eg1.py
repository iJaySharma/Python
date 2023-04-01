import array as arr
class MyInt:
  def __init__(self,num):
     self.x=num
  def __add__(self,other):
     return MyInt(self.x+other.x)
  def __str__(self):
    return str(self.x)
x=MyInt(10)
y=MyInt(20)
z=x+y
print(z)


x=arr.array('i')
y=range(5)
for i in y: x.append(int(input("Enter a number : ")))