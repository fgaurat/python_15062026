


class Rectangle:


    def __init__(self,longueur:int,largeur:int):
        assert longueur>0 and largeur>0
        self._longueur:int = longueur
        self._largeur:int = largeur


    def surface(self):
        return self._longueur*self._largeur
    
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        assert longueur > 0
        self._longueur = longueur
 
    def set_largeur(self,largeur):
        assert largeur > 0
        self._largeur = largeur
    
    def __str__(self):
        return f"{__class__.__name__} longueur:{self._longueur}, largeur:{self._largeur}"
    
    def __eq__(self, value) -> bool:
        return self._longueur == value._longueur and self._largeur == value._largeur
    
    longueur = property(get_longueur,set_longueur,doc="La longueur")
    largeur = property(get_largeur,set_largeur,doc="La largeur")