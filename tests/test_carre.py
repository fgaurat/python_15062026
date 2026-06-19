import pytest
from carre import Carre


def test_init_sets_cote_and_dimensions():
    carre = Carre(5)

    assert carre.cote == 5
    assert carre.longueur == 5
    assert carre.largeur == 5


def test_cote_setter_updates_longueur_and_largeur():
    carre = Carre(2)

    carre.cote = 9

    assert carre.cote == 9
    assert carre.longueur == 9
    assert carre.largeur == 9


def test_multiple_cote_updates_keep_square_invariant():
    carre = Carre(1)

    for value in (3, 7, 10):
        carre.cote = value
        assert carre.cote == value
        assert carre.longueur == value
        assert carre.largeur == value


@pytest.mark.parametrize("invalid_value", [0, -1, -10])
def test_cote_setter_rejects_non_positive_values(invalid_value):
    carre = Carre(4)

    with pytest.raises(AssertionError):
        carre.cote = invalid_value


@pytest.mark.parametrize("invalid_value", [0, -2])
def test_init_rejects_non_positive_values(invalid_value):
    with pytest.raises(AssertionError):
        Carre(invalid_value)