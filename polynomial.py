from math import sqrt
import matplotlib.pyplot as plt  # type:ignore
import numpy as np


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = {ex: ce for ex, ce in enumerate(coeffs[::-1])}

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        assert type(other) is Poly2
        sol = Poly2(0)
        sol.coeffs = {**self.coeffs}
        for ex, ce in other.coeffs.items():
            sol.coeffs[ex] = sol.coeffs.get(ex, 0) + ce
        return sol

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        assert type(other) is Poly2
        sol = Poly2(0)
        sol.coeffs = {**self.coeffs}
        for ex, ce in other.coeffs.items():
            sol.coeffs[ex] = sol.coeffs.get(ex, 0) - ce
        return sol

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        sol = [""] + [f"{ce}x^{i}" for i, ce in sorted(self.coeffs.items()) if ce] + [""]
        sol = "+".join(reversed(sol))
        sol = sol.replace("+1x", "+x")
        sol = sol.replace("-1x", "-x")
        sol = sol.replace("x^0", "")
        sol = sol.replace("x^1+", "x+")
        sol = sol.replace("+-", "-")
        sol = sol.strip("+")
        sol = sol.replace("+", " + ")
        sol = sol[:1] + sol[1:].replace("-", " - ")
        return sol.strip()

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        taille = len(self.coeffs)
        if taille == 1:
            a = self.coeffs[0]
            b = 0
            c = 0
        elif taille == 2:
            a = self.coeffs[0]
            b = self.coeffs[1]
            c = 0
        elif taille == 3:
            a = self.coeffs[0]
            b = self.coeffs[1]
            c = self.coeffs[2]
        else:
            a = 0
            b = 0
            c = 0

        if taille > 0:

            delta = b**2 - 4 * a * c
            if delta > 0:
                rDeDelta = sqrt(delta)
                retour = [(-b - rDeDelta) / (2 * a), (-b + rDeDelta) / (2 * a)]
            elif delta < 0:
                r1 = complex(-b/(2*a),sqrt(-delta)/(2*a))
                r2 = complex(-b/(2*a),-sqrt(-delta)/(2*a))
                retour = [r1, r2]

            else:
                retour = [-b / (2 * a)]
            return retour

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        taille = len(self.coeffs)
        if taille == 1:
            y = self.coeffs[0]* (x**2)
        elif taille == 2:
            y = self.coeffs[0]* (x**2) + self.coeffs[1]*x
        elif taille == 3:
            y = self.coeffs[0]* (x**2) + self.coeffs[1]*x + self.coeffs[2]
        else:
            y = 0

        return y



    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        x = np.arange(0, 11, 1)
        y = self.__val(x)
        plt.scatter(x,y)
        plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    p4 = p1 - p2
    print(p3)  # affiche 2x^2 + 2x + 2
    print(p4)

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
