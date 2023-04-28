k=(101,"Suresh","Goa")
print(k)
print(type(k))
print(k[0])
print(k[1])
print(k[2])
for e in k: print(e)
# k[0]=102 immutable
print(k.index("Suresh"))
print(k.count("Suresh2"))
print(101 in k)
t=(25) # not a tuple
m=(25,) # tuple
print(m)
print(type(m))
k=k+m
print(k)
f=(101,"Jay","Pune")
(roll_number,name,city)=f
print(type(roll_number),roll_number)
print(type(name),name)
print(type(city),city)
l=(101,"sasa","goa",25,"thomas")
print(l)
m=k[1:4]
print(type(m),m)
m=l[1:]
print(m)
m=l[:4]
print(m)