
from rectangle import Rectangle

class Carre(Rectangle):
    

    def __init__(self, cote: int):
        super().__init__(cote, cote)
        self._cote = cote

    @property
    def cote(self):
        return self._cote
    

    @cote.setter
    def cote(self,cote):
        assert cote >0
        self.longueur = cote
        self.largeur = cote
        self._cote = cote
