
from icalcgeo import ICalcGeo
import math
class Cercle(ICalcGeo):
    

    def __init__(self, rayon: int):
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon
    

    @rayon.setter
    def rayon(self,rayon):
        assert rayon >0
        self._rayon = rayon

    @property
    def surface(self):
        return math.pi*self._rayon**2