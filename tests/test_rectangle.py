import pytest
import sys

from rectangle import Rectangle




def test_init_rectangle():
    # AAA
    
    # Arrange
    # Act
    # Assert


    r = Rectangle(1,2)
    assert r


def test_surface():
    # AAA
    
    # Arrange
    r = Rectangle(1,2)
    
    # Act
    surface = r.surface
    
    # Assert
    assert surface == 2

def test_nouveau_rectangle_leve_une_erreur():
    # AAA
    
    # Arrange
    # Act
    # Assert
    with pytest.raises(AssertionError):
        r = Rectangle(-1,2)


@pytest.mark.parametrize(
    "longueur, largeur, surface_attendue",
    [
        (1, 2, 2),
        (3, 4, 12),
        (5, 6, 30),
    ]
)
def test_surface_avec_parametres(longueur, largeur, surface_attendue):
    # AAA
    
    # Arrange
    r = Rectangle(longueur, largeur)
    
    # Act
    surface = r.surface
    
    # Assert
    assert surface == surface_attendue
