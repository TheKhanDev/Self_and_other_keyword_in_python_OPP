print("TASK 01:\n")
class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"({self.real}, {self.imag})"


# Testing
c1 = Complex(3, 4)
c2 = Complex(1, 2)

print("Complex 1:", c1)
print("Complex 2:", c2)

print("Addition:", c1.add(c2))
print("Subtraction:", c1.subtract(c2))

print("Task 02:\n") 
import math

class Rational:
    def __init__(self, num=0, den=1):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def add(self, other):
        return Rational(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def subtract(self, other):
        return Rational(self.num * other.den - other.num * self.den,
                        self.den * other.den)

    def multiply(self, other):
        return Rational(self.num * other.num,
                        self.den * other.den)

    def divide(self, other):
        return Rational(self.num * other.den,
                        self.den * other.num)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def to_float(self):
        return self.num / self.den


# Testing
r1 = Rational(2, 4)
r2 = Rational(3, 5)

print("Rational 1:", r1)
print("Rational 2:", r2)

print("Add:", r1.add(r2))
print("Subtract:", r1.subtract(r2))
print("Multiply:", r1.multiply(r2))
print("Divide:", r1.divide(r2))
print("Floating:", r1.to_float())



print("TASK 03:")
class HugeInteger:
    def __init__(self, num="0"):
        self.num = num

    def add(self, h):
        return HugeInteger(str(int(self.num) + int(h.num)))

    def sub(self, h):
        return HugeInteger(str(int(self.num) - int(h.num)))

    def show(self):
        print(self.num)


# Test
h1 = HugeInteger("99999999999999999999")
h2 = HugeInteger("11111111111111111111")

print("Add:")
h1.add(h2).show()

print("Sub:")
h1.sub(h2).show()
