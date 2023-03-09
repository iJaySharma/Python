a=10
b=20
c=30
print("Total of",a,"and",b,"is",c)
print("Total of %d and %d is %d" %(a,b,c))
print("Total of {} and {} is {}".format(a,b,c))
print("Total of {} and {} is {}".format(c,b,a))
print("Total of {1} and {2} is {0}".format(c,a,b))
print("Total of {num1} and {num2} is {num3}".format(num3=c,num2=b,num1=a))
print(f"Total of {a} and {b} is {c}")