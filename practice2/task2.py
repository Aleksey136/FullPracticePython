def function(line):
    line2 = str(bin(line))
    while len(line2) != 34:
        line2 = "0b0" + line2[2:]
    A = line2[22:]
    B = line2[10:22]
    C = line2[4:10]
    D = line2[3]
    E = line2[2]
    line2 = "0b" + D + A + B + E + C
    return hex(int(line2, 2))


if __name__ == '__main__':
    inputUser = 0x78c3a3b4
    print(function(inputUser))
    inputUser = 0x8f6e6557
    print(function(inputUser))
