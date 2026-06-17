print("Hello, world!")

# HelloWorld UpperCamelCase/ PascalCase
# helloWorld camelCase
# hello-world kebab-case
# hello_world snake_case

the_world_is_flat:bool = True
if the_world_is_flat:
    a = 'Be careful not to fall off!'
    print(a) 
    
# if( the_world_is_flat){
#     print("Be careful not to fall off!")
# }

s = 'L\'orage gronde'
s = "L\'orage gronde"

print(s)

p = "c:\\test\\new_project"
p = r"c:\test\new_project"
print(p)

lines = """ligne 1

ligne 2
ligne 3
"""
print(lines)



print("-" * 50)

a = 2
print("la valeur de a est : " + str(a))

a = 2
print("la valeur de a est : " * a)

print("-" * 50)
p = "Python"
print(p[0])
print(len(p))

print(p[len(p)-1])
print(p[-1])

# slicing
print(p[0:2]) # affiche les caractères d'index 0 et 1.   [0:2[
print(p[2:4])
print(p[4:5])
print(p[:2]) # implicitement 0
print(p[2:]) # implicitement len(p)
print(p[:]) # implicitement 0 et len(p)


squares = [1, 4, 9, 16, 25]
squares = squares + [36, 49, 64, 81, 100]
print(squares)
# s = str(squares)
# print(s)


a = 1
b = 1
print(hex(id(a)))
print(hex(id(b)))


a = 2
print(a)
print(hex(id(a)))
print(hex(id(b)))

a = 12344535436234223423
b= 12344535436234223423
import sys
print(sys.getrefcount(a))




squares = [1, 4, 9, 16, 25]
p = "Python"
print(squares[0])
print(p[0])
squares[0] = 12
# p[0] = 'j'
squares.append(36)
print(squares)



squares = [1, 4, 9, 16, 25]
# squares2 = [1, 4, 9, 16, 25]
squares2 = squares
# squares2 = squares.copy()
# squares2 = squares[:]
squares[0] = 12

print(squares) # [12, 4, 9, 16, 25]
print(squares2) # [1, 4, 9, 16, 25]

l3 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
l4 = l3[:]
l4 = l3.copy()
import copy
l4 = copy.deepcopy(l3)
l3[0][0] = 100
print(l3) 
print(l4) 


# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a)
    c = a+b
    a, b = b, c