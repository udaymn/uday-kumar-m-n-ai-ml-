a=lambda x:x+5
print(a(2))

b= lambda a,b:a+b
print(b(2,3))


c=lambda a,b : a if (a>b) else b
d=lambda x: x**2
print(d(4))

#map
lst=[1,2,3,4,5]
l=list(map(lambda x:x+5,lst))
print(l)

#filter
lst=[1,2,3,4,5,6]
l=list(filter(lambda x:x%2,lst))
print(l)

#reduce
lst=[1,2,3,4,5]
from functools import reduce
y=reduce(lambda x,y:x+y,lst)
print(l)
