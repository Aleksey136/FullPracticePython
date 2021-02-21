def output(matrixUser):
    for i in range(len(matrixUser)):
        for j in range(len(matrixUser[i])):
            print(matrixUser[i][j], end="\t\t")
        print()


def function(matrix):
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
    output(matrix)


if __name__ == '__main__':
    inputUser = [[None, None, None], [None, None, None], ["06/11/2001;Мибберг Артемий", "0.17", "+77009999725"],
                 ["20/10/2002;Шуфян Иван", "0.15", "+78336729824"], ["22/09/1999;Футук Эмиль", "0.69", "+75121041454"]]
    function(inputUser)
    print()
    inputUser = [["21/01/2004;Сигко Филипп", "0.54", "+78887971326"],
                 ["14/09/1999;Лучабий Александр", "0.35", "+78657666161"],
                 ["13/05/2001;Лазук Елисей", "0.13", "+79251288655"], [None, None, None],
                 ["20/02/1999;Мицибко Родион", "0.69", "+71293479061"]]
    function(inputUser)
