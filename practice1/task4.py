import math


def function(nFunc):
    output = float(0)
    if nFunc == 0:
        output = 7
    else:
        output = 1 / 95 * function(nFunc - 1) + math.tan(function(nFunc - 1))
    return output


if __name__ == '__main__':
    n = int(input("Введите n: "))
    print("f(" + str(n) + ") = {:.2e}".format(function(n)))
