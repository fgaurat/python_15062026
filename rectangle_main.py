from rectangle import Rectangle
from carre import Carre
from cercle import Cercle

def main():
    
    r = Rectangle(12,3)
    

    # print(r.get_longueur())
    # print(r.get_largeur())
    print(r.longueur)
    print(r.largeur)
    
    # r.longueur = -12
    # r.set_longueur(12)
    print(r.surface)
    
    s = str(r)
    print(s)

    r1 = Rectangle(12,3)
    r2 = Rectangle(12,3)

    if r1==r2:
        print("ok")
    else:
        print("ko")
    
    print(50*'-')
    
    c = Carre(2)
    print(c.cote)
    print(c.surface)
    c.cote = 3
    print(c.cote)
    print(c.surface)
    print(50*'-')
    ce = Cercle(2)
    print(ce.surface)

if __name__=='__main__':
    main()
