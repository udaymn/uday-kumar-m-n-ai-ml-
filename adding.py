a=[1,1,1]
b=[1,2,3,4]
c=[1,1,1]
x=list(map(lambda x,y,z:x+y+z,a,b,c))
print(x)

fruits=['mango','apple','orange','banana','kiwi']
l=list(filter(lambda x:'m'in x,fruits))
print(l)
