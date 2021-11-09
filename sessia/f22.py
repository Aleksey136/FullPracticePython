def function(line):
    line2 = ((line >> 4) & 0x1fff) << 19
    line2 = line2 | ((line & 0x0000000f) << 15)
    line2 = line2 | (((line >> 17) & 0x7fff) << 0)
    return hex(line2)


if __name__ == '__main__':
    x = 0x62d2b22c
    print(function(x))
