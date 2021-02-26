def function(line: hex):
    line2 = ((line >> 30) & 0x1) << 31
    line2 = line2 | ((line & 0x00000fff) << 19)
    line2 = line2 | (((line >> 12) & 0xfff) << 7)
    line2 = line2 | (((line >> 31) & 0x1) << 6)
    line2 = line2 | ((line >> 24) & 0x3f)
    return hex(line2)


if __name__ == '__main__':
    x = 0x8f6e6557
    print(function(x))
