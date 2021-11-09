import math


def f13(n, m):
    a = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = a + math.log(j) - j * j * j * j - 45
    a = 84 * a
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = a - (33 * i - 88 * j ** 6)
    return a


if __name__ == '__main__':
    print("{:.2e}".format(f13(25, 63)))
