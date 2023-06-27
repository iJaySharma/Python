import array as arr
class DimensionError(Exception):
   def __init__(self,exception):
      self.exception=exception
class TMArray: 
   def __init__(self,rows,columns):
      if rows<=0 or columns<=0: raise DimensionError(f"Invalid dimension [{rows}][{columns}]")
      self.rows=rows
      self.columns=columns
      self.x=arr.array('i')
      for i in range(rows*columns): self.x.append(0)
   def __str__(self):
      for r in range(self.rows):
         for c in range(self.columns):
            print("%10d"%(self.x[(r*self.columns)+c]),end="")

         print()
      return ""
x=TMArray(5,3)
print(x)