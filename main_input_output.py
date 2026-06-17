def main():
    a= 2
    b = 3
    c = a/b

    print(c)
    # f-string
    result = f" a={a} / b={b} = c=>{c}"
    print(result)
    result = f" a={a} / b={b} = c=>{c*100:.2f}%"
    result = f" a={a} / b={b} = c=>{c:.2%}"
    result = f" {a=} / {b=} = c=>{c=:.2%}"
    print(result)

    l = [a,b,c]
    v = " valeur de a:{}, valeur de b:{}, valeur de c:{}".format(a,b,c)
    v = " valeur de a:{0}, valeur de b:{1}, valeur de c:{2}".format(a,b,c)
    v = " valeur de a:{0}, valeur de b:{1}, valeur de c:{2:.2}".format(*l)
    print(v)
    d = {
        "name":"Gaurat",
        "firstname":"Fred"
    }
    s = "Bonjour {name}, {firstname}".format(name=d['name'],firstname=d['firstname'])
    s = "Bonjour {n}, {f}".format(n=d['name'],f=d['firstname'])
    s = "Bonjour {name}, {firstname}".format(**d)
    print(s)


    f = open('le_fichier.txt',"a") # a: append, w: write
    f.write('Une ligne\n')
    f.write('Une autre ligne\n')
    f.close()

    # f = open('le_fichier.txt',"r") 
    f = open('le_fichier.txt')# lecture par défaut
    
    # Totalité du fichier dans une var
    # s = f.read()
    # lines = s.splitlines()
    # for line in lines:
    #     print(line)
    
    # lines = f.readlines()
    # for line in lines:
    #     print(line.strip())
    
    for line in f:
        print(line.strip())

    f.close()


    with open('le_fichier.txt') as f:
        for line in f:
            print(line.strip())

    




if __name__=='__main__':
    main()
