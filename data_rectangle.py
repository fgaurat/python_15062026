
from dataclasses import dataclass


@dataclass
class DataRectangle:
    longueur:int=0
    largeur:int=0

    @property
    def surface(self):
        return self.longueur*self.largeur


def main():
    d = DataRectangle(2,4)
    d1 = DataRectangle(2,4)
    print(d.longueur)
    print(d.largeur)
    d.longueur = 12
    print(d)

    if d == d1:
        print("ok !") 

if __name__=='__main__':
    main()
