from icalcgeo import ICalcGeo


class Rectangle(ICalcGeo):


    def __init__(self,longueur:int,largeur:int):
        assert longueur>0 and largeur>0
        self._longueur:int = longueur
        self._largeur:int = largeur

    @property
    def surface(self):
        return self._longueur*self._largeur
    
    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self,longueur):
        assert longueur > 0
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur > 0
        self._largeur = largeur
    
    def __str__(self):
        return f"{__class__.__name__} longueur:{self._longueur}, largeur:{self._largeur}"
    
    def __eq__(self, value) -> bool:
        return self._longueur == value._longueur and self._largeur == value._largeur
    
