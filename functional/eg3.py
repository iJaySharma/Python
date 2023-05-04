import time as tt
import random as rr
def add(t):
   return t[0]+t[1]
lst=[]
y=1
while y<=100000:
   lst.append((rr.randrange(10000),rr.randrange(100000)))
   y=y+1
ts=tuple(lst)
print(ts)
sum=[]
start=tt.time_ns()
for i in ts:
 sum.append(add(i))
end=tt.time_ns()
print("Time taken in nano seconds : ",end-start)
print(f"sum of {ts[0]} is {sum[0]}")
print(f"sum of {ts[1]} is {sum[1]}")

# alternative method 

import time as tt
import random as rr
def add(t):
   print("Add got called with argument as",t)
   return t[0]+t[1]
lst=[]
y=1
while y<=100000:
   lst.append((rr.randrange(10000),rr.randrange(100000)))
   y=y+1
ts=tuple(lst)
print(ts)
start=tt.time_ns()
rs=map(add,ts)
end=tt.time_ns()
print("Time taken in nano seconds : ",end-start)
k=rs.__iter__()
print(type(rs),type(k))
sum1=k.__next__()
sum2=k.__next__()
print(f"sum of {ts[0]} is {sum1}")
print(f"sum of {ts[1]} is {sum2}")











