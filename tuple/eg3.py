import collections as coll
a = coll.namedtuple("Student","roll_number name city")
student1 = a(101,"Suresh","Ujjain")
print(student1)
print(type(student1))

student1.__init__(roll_number=105,city="Ujjain",name="Mohan",x=4)
print(student1)
print(student1[0])
class aaa:
   def __init__(self,a,b,c):
      print(a,b,c)
k=aaa(10,20,30)