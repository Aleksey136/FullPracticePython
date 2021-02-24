def function(line):
    line2 = str(bin(int(line, 16)))
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
    inputUser = input()
    print(function(inputUser))
