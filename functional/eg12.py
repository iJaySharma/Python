class HeaderAdder:
  def __init__(self,f):
    self.f=f
  def __call__(self):
    print("some heading")
    self.f()
  
@HeaderAdder
def report():
  print("cool")

report()


class HeaderAdder:
  def __init__(self,heading):
    self.heading=heading
  def __call__(self,f):
     def withHeader():
        print(self.heading)
        f()
     return withHeader
  
@HeaderAdder("Weather Report")
def report():
  print("Today will be shiny day")

report()