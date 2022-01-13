from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""
    def __init__(self, coeffa, coeffb, coeffc):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.a = coeffa
        self.b = coeffb
        self.c = coeffc

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        if isinstance(other, Poly2):
            return Poly2(self.a + other.a, self.b + other.b, self.c + other.c)
        else :
            return Poly2(self.a, self.b, self.c + other)

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        if isinstance(other, Poly2):
            return Poly2(self.a - other.a, self.b - other.b, self.c - other.c)
        else :
            return Poly2(self.a, self.b, self.c - other)

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        s = "{0.a}X^2+{0.b}X+{0.c}".format(self)
        return s

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        d = (self.b ** 2) - (4 * self.a * self.c)
        res1 = (-self.b - sqrt(d)) / (2 * self.a)
        res2 = (-self.b - sqrt(d)) / (2 * self.a)
        return res1,res2

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        val = self.a * x ** 2 + self.b * x + self.c
        return val

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        polyCoeffiecients = [self.a,self.b,self.c]
        plt.plot(polyCoeffiecients)
        plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
