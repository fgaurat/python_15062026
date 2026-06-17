t = (1,2,"toto",2.4)
print(t)
# t[0]=0

# a,b = (1,2)
# a,b,*lereste = 1,2,3,4,5,6
a,b = (1,2,3),(4,5,6)
print(a,b)

a,*lereste,b,c = 1,2,3,4,5,6
print(a,lereste,b,c)

l = [1,2,3]
a,b,c = l
print(a,b,c)
a,*b,c = 12,*l,23 # 12,1,2,3,23
print(a,b,c)


a=2,
b=3,
c = a,b
print(c)

a = set('abracadabra')
b = set('alacazam')

print(a,b)