import math


def function(xFunc):
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


if __name__ == '__main__':
    x = float(input())
    print("{:.2e}".format(function(x)))
