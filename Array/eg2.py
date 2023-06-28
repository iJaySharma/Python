class aaa:
   def __getitem__(self,index):
      print("getitem got called with argument as ",index)
      return "Ujjain"
   def __setitem__(self,index,item):
      print("setitem got called with index : ",index,"and item : ",item)

a=aaa()
print(a[0])
print("*"*50)
a[2]=30