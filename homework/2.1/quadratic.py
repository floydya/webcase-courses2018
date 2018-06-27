import cmath
import math
import sys


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else: # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)


equation = list()
equation.append("{0:.0f}x\N{SUPERSCRIPT TWO}".format(a))
equation.append("-") if b < 0 else equation.append("+")
equation.append("{0:.0f}x".format(abs(b)))
equation.append("-") if c < 0 else equation.append("+")
equation.append("{0:.0f} = 0 \N{RIGHTWARDS ARROW} x = {1}".format(abs(c), x1))
if x2 is not None:
    equation.append("or x = {0}".format(x2))


print(" ".join(equation))
