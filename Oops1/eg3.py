class Bulb: 
  def setWattage(j,e):
    j.wattage=e   
  def getWattage(m):
       return m.wattage
  def __str__(u):
       return "Cool Bulb"
k=Bulb()
k.setWattage(60)
print("Wattage is : ",k.getWattage())
r=Bulb()
r.setWattage(100)
print("Wattage is : ",r.getWattage())
"""
p=Bulb()
print(p.wattage)
print(p.getWattage)
"""
j=Bulb()
print(type(j))
print(j)