"""Petit module de calcul autour de la suite de Fibonacci."""


def fib(n: int) -> list[int]:
    """Retourne tous les nombres de Fibonacci strictement inferieurs a n."""
    a, b = 0, 1
    values: list[int] = []
    while a < n:
        values.append(a)
        a, b = b, a + b
    return values


def somme(values: list[int]) -> int:
    """Calcule la somme des valeurs numeriques d'une sequence."""

    s = 0
    for x in values:
        s = s + x
    return s


if __name__ == "__main__":
    print(fib(1000))
    print("somme =", somme(fib(1000)))
