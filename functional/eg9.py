def lmn(x):
   if x==4: return 
   lmn(x+1)
   print(x)

lmn(1)

def Imn(p):
  if p==1: return 1
  n=p*Imn(p-1)
  return n
print(Imn(5))

def pow(b,p):
  if p==0: return 1
  return b*pow(b,p-1)

print(pow(10,4))