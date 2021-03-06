def f21(x):
    output = -1
    if x[0] == "tea":
        if x[4] == "2010" or x[4] == 2010:
            if x[1] == "2000" or x[1] == 2000:
                output = 0
            elif x[1] == "1996" or x[1] == 1996:
                output = 1
            elif x[1] == "2014" or x[1] == 2014:
                if x[3] == "vue":
                    output = 2
                elif x[3] == "numpy":
                    output = 3
        elif x[4] == "1980" or x[4] == 1980:
            if x[3] == "vue":
                output = 4
            elif x[3] == "numpy":
                if x[1] == "2000" or x[1] == 2000:
                    output = 5
                elif x[1] == "1996" or x[1] == 1996:
                    output = 6
                elif x[1] == "2014" or x[1] == 2014:
                    output = 7
        elif x[4] == "1992" or x[4] == 1992:
            output = 8
    elif x[0] == "m4":
        output = 9
    elif x[0] == "csv":
        output = 10
    return output


def f22(line):
    line2 = ((line >> 30) & 0x1) << 31
    line2 = line2 | ((line & 0x00000fff) << 19)
    line2 = line2 | (((line >> 12) & 0xfff) << 7)
    line2 = line2 | (((line >> 31) & 0x1) << 6)
    line2 = line2 | ((line >> 24) & 0x3f)
    return int(line2)


def f23(matrix):
    matrix2 = []
    for i in range(len(matrix)):
        flag = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] is None:
                flag = flag + 1
        if flag != 3:
            matrix2.append(matrix[i])
    matrix = []
    for i in range(len(matrix2)):
        a = "{6}{7}{8}{9}/{3}{4}/{0}{1}".format(*matrix2[i][0].split(";")[0])
        b = matrix2[i][0].split(";")[1]
        c = b.split(" ")[0]
        matrix.append([c, str(round(float(matrix2[i][1]), 1)), a,
                       "{5}{6}{7}-{8}{9}-{10}{11}".format(*matrix2[i][2])])
    matrix.sort(key=lambda x: x[3])
    return matrix
