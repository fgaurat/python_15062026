

l =[10,20,30,40,50]
print(l)

l.append(60)


print(l)
last_value = l.pop()
print(l,"last_value",last_value)
l.insert(0,-10)
print(l)
first_value = l.pop(0)
print(l,"first_value",first_value)
# l.remove(50)
print(50*'-')
from collections import deque
d = deque(l)
print(d)
d.append(60)
print(d)
d.appendleft(-10)
d.appendleft(50)
print(d)
print(d.count(50))
print(50*'-')


l =[10,20,30,40,50]
result = []
for i in l:
    result.append(i*2)
print(result)

# l2 = list(map(lambda i:i*2,l))
# print(l2)
result = [i*2 for i in l if i <= 40]
print(result)

lines = [" _ligne 01_  ","ligne 02 ","    ligne 03"]
clean_lines = [l.strip("1 _") for l in lines]


print(lines)
print(clean_lines)
# a = "   chaine moche.  "lines 
# print(a.strip())
del clean_lines[0]
print(clean_lines)

