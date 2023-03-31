import array
a=array.array('i')
a.append(2147483647)# yess
a.append(2147483648)# no
a.append(-2147483648)# yess
a.append(-2147483649)# no
a.append(-30)
print(a[0])
print(a[1])