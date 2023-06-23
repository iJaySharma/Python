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