def hcf(x, y):
    x, y = abs(x), abs(y)
    hcf = x if x < y else y
    r = x% y
    while (r != 0):
        x = y
        y = r
        r =x % y
    return y
class Fraction:
    def __init__(self,nr,dr):
        self.nr = nr
        self.dr = dr
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")

        if dr < 0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

        self._reduce()

    def __repr__(self):
        return "0" if self.nr == 0 else str(self.nr) if self.dr == 1 else f"{self.nr}/{self.dr}"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def _reduce(self):
        n = hcf(self.nr, self.dr)

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)


Fraction_1 = Fraction(4, 5)
Fraction_2 = Fraction(3, -2)

print("Phân số đã nhập: ",Fraction_1, Fraction_2)
print("-"*50)

print("Tổng 2 p/s = ",Fraction_1 + Fraction_2)
print("Hiệu 2 p/s = ",Fraction_1 -Fraction_2)
print("Tích 2 p/s = ",Fraction_1 * Fraction_2)
print("Chia 2 p/s = ",Fraction_1 / Fraction_2)

print("-"*50)

print("p/s 1 + 3 = ",Fraction_1 + 3)
print("p/s 1 - 0.5 = ",Fraction_1 - 0.5)
print("p/s 2 * 2 = ",Fraction_2 * 2)
print("p/s 2/2= ",Fraction_2 / 2)


