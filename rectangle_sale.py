from   dataclasses import dataclass
import json

class rectangle :
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur =largeur
    def Surface(self) :
        return self.longueur*self.largeur
    def __str__(self): return "rectangle %s x %s"%(self.longueur,self.largeur)

if __name__=="__main__":
    r=rectangle(3,4)
    print(r,"->",r.Surface())


