class TMRange:
    def __init__(k,start,end,step=1):
        k.start=start
        k.end=end
        k.current=k.start
        k.step=step
    def __str__(k):
       return f"TMRange({k.start},{k.end})"
    def __iter__(k):
       return k
    def __next__(k):
      if k.current>k.end: raise StopIteration
      data=k.current
      k.current=k.current+k.step
      return data 
x=TMRange(1,10,2)
print(x)
for u in x:
   print(u)


""" nahi chalega iter method nai h
class TMRange:
    def __init__(k,start,end,step=1):
        k.start=start
        k.end=end
        k.current=k.start
        k.step=step
    def __str__(k):
       return f"TMRange({k.start},{k.end})"
x=TMRange(1,10,2)
print(x)
for u in x:
   print(u)
"""
