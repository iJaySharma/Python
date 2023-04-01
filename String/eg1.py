import array as aaa
a = aaa.array("i")
a.append(10)
a.append(20)
a.append(30)
a.append(20)
a.append(50)
while True:
  try:
      a.remove(20)
  except:
      break
for x in a: print(x)