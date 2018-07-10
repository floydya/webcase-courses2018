import math


def checkio(a, b, c):

    if (a + b) > c:
        first = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2)/(2 * a * b)))
        second = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2)/(2 * a * c)))
        third = math.degrees(math.acos((c ** 2 + b ** 2 - a ** 2)/(2 * c * b)))
        return sorted([round(first), round(second), round(third)])
    else:
        return [0, 0, 0]