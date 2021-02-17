import math


def function(nFunc, mFunc):
    f = float(0)
    for i in range(1, nFunc + 1):
        for j in range(1, mFunc + 1):
            f += 47 * (math.tan(i) + 50 * j ** 2)
        f += 62 * (math.exp(i) + 84 * i ** 3)
    return f


if __name__ == '__main__':
    n = int(input("Введите n: "))
    m = int(input("Введите m: "))
    print("f(" + str(n) + ", " + str(m) + ") = {:.2e}".format(function(n, m)))
