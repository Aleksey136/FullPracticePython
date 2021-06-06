..import math


def f11(xFunc, yFunc):
    return math.sqrt(xFunc ** 6 / 2 + 70 * xFunc ** 7) + math.sqrt(yFunc ** 2 - 97 * yFunc ** 7) + math.sqrt(
        (math.exp(xFunc) - 13 * yFunc ** 4) / (xFunc - yFunc ** 5))


def f12(xFunc):
    f = float(0)
    if xFunc < 21:
        f = (xFunc ** 6) / 32 + math.fabs(xFunc)
    elif 21 <= xFunc < 54:
        f = 94 * xFunc ** 6 - (xFunc ** 3) / 28 - xFunc ** 4
    elif 54 <= xFunc < 109:
        f = xFunc - 5 * xFunc ** 5
    else:
        f = 68 * xFunc ** 3 + xFunc ** 2 - 73
    return f


def f13(nFunc, mFunc):
    f2 = float(0)
    for i in range(1, nFunc + 1):
        for j in range(1, mFunc + 1):
            f2 += 47 * (math.tan(i) + 50 * j ** 2)
        f2 += 62 * (math.exp(i) + 84 * i ** 3)
    return f2


def f14(nFunc):
    output = float(0)
    if nFunc == 0:
        output = 7
    else:
        output = 1 / 95 * f14(nFunc - 1) + math.tan(f14(nFunc - 1))
    return output
