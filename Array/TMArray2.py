import array as arr
class DimensionError(Exception):
   def __init__(self,exception):
      self.exception=exception
class TMArrayRow: 
   def __init__(self,x,startIndex,endIndex):
      self.x=x
      self.startIndex=startIndex
      self.endIndex=endIndex
   def __getitem__(self,index):
      return self.x[self.startIndex+index]
   def __setitem__(self,index,item):
      self.x[self.startIndex+index]=item
class TMArray:
   def __init__(self,rows,columns):
      if rows<=0 or columns<=0: raise DimensionError(f"Invalid dimension [{rows}][{columns}]")
      self.rows=rows
      self.columns=columns
      self.x=arr.array('i')
      for i in range(rows*columns): self.x.append(0)
   def __str__(self):
      ss=""
      for r in range(self.rows):
         for c in range(self.columns):
            ss=ss+("%10d"%(self.x[(r*self.columns)+c]))
         ss+="\n"
      return ss
   def __getitem__(self,rowIndex):
      startIndex=rowIndex*self.columns
      endIndex=startIndex+self.columns-1
      return TMArrayRow(self.x,startIndex,endIndex)
   def transpose(self):
      t=TMArray(self.columns,self.rows)
      for r in range(self.columns):
         for c in range(self.rows):
            t[r][c]=self[c][r]
      self.x=t.x
      self.rows=t.rows
      self.columns=t.columns
 
x=TMArray(3,2)
print(x)
x[0][0]=1
x[0][1]=2
x[1][0]=3
x[1][1]=4
x[2][0]=5
x[2][1]=6
print(x)
x.transpose()
print(x)