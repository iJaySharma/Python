# Composition

def AinB(str1,str2):
   k=[]
   for i in str1:
      if i in str2 and i not in k: k.append(i)
   return k
 
def GetUnicodes(coll):
   m=[]
   for i in coll: m.append(ord(i))
   return m


def Composer(f1,f2):
   def compose(str1,str2):
      return f2(f1(str1,str2))
   return compose;
  
a=Composer(AinB,GetUnicodes)
b=a("good bread","god is great")
print(b)
