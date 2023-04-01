a="abcdabcdabcd"
print(a.count("ab"))
print(a.count("ab",2))
print(a.count("ab",2,7))

print(a.find("ab"))
print(a.find("ab",2))
print(a.find("kk"))

print(a.index("ab"))
print(a.index("ab",2))
#print(a.index("ll")) ye exception generate karega

a="abcd1234"
b="abcd"
c="1234"
d=",!#"
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

