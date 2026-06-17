# n = input('Votre nom:')
# print(type(n))

# a:str= input('Votre année de naissance:')

# print(2026  - int(a) )

print(50*'-')
l = ['Value 01', 'Value 02', 'Value 03', 'Value 04', 'Value 05']

for value in l:
    print(value)

for i in range(len(l)):
    if i == 1:
        continue
    print(i, l[i])

    if i == 2:
        break


to_find = 5

for i in range(10):

    if i == 15:
        break
else:
    pass



print(50*"-")


def http_error(status:int)->str:
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error("400"))

print("-"*50)
point = (12,3)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")



print(50*'-')
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result=[]

    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

# Now call the function we just defined:
fib(2000)
r = fib2(2000)
print(r)# [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ]



def hello(name,first_name,age,job):
    print(name,first_name,age,job)



# hello("Gaurat","Fred") # par position
# hello(first_name="Fred",name="Gaurat")# mots-clefs
# hello("Fred")
# hello("Gaurat","Fred",name="dev",age=49)

print(50*'-')
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
print(50*'-')



def f(value):
    arg=[]
    arg.append(value)
    return arg
r = f(1)
print(r) # 1
r = f(2)
print(r) # ?



print(50*'-')
a = 2

def f():
    # global a
    a=1000    
    if False:
        a=1000    
    # print("2?",a)
    print(a) # 1000

print("avant",a) #2
f() # 1000
print("après",a) #2

print(50*'-')






def add(*values): # nombre variable de paramètre passés par position
    print(values)
    s = 0
    for v in values:
        # s =s+v
        s +=v
    return s

l =[10,20,30,40,50]
r = add(*l) # [10,20,30,40,50] => 10,20,30,40,50
# r = add(10,20,30,40,50) 
print(r) # 150


# def hello(**kwargs):
def hello(name,firstname,/):    # pos1, pos2, / -> Positional only
                                # *, kwd1, kwd2 -> Keyword only
    # print(kwargs['nametoto'])
    print(name,firstname)

# hello(name="Gaurat",firstname="fred")
# hello("Gaurat","fred")


a = 2
b =3
c=4
print("valeur de a:",a,b,c,sep=",")


def mult2(l):
    result = []
    for i in l:
        result.append(i*2)
    return result

def mult2_item(i):
    return i*2

print(50*'-')
l =[10,20,30,40,50]
l2 = mult2(l)
print(l2) # [20,40,60,80,100]

# (i):i*2
#     

# l2 = list(map(mult2_item,l))
l2 = map(lambda i:i*2,l)
# l2 = list(map(lambda i:i*2,l))
print(l2)
for i in l2:
    print(i)








def sum(a):
    print(a)

r = sum([1,2,3])

print(r)