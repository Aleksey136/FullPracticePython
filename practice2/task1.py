def function(x):
    output = -1
    if x[1] == "hy":
        if x[0] == "eq":
            if x[3] == 2016:
                output = 0
            elif x[3] == 1957:
                output = 1
        elif x[0] == "lex":
            if x[3] == 2016:
                output = 2
            elif x[3] == 1957:
                output = 3
    elif x[1] == "bro":
        output = 4
    return output


if __name__ == '__main__':
    # xUser = [str, str, str, int]
    # print("Вводите через <enter>:")
    # for i in range(0, 4):
    #     xUser[i] = input()
    xUser = ['lex', 'hy', 'hy', 1957]
    print("f(['lex', 'hy', 'hy', 1957]) = " + str(function(xUser)))
    xUser = ['lex', 'hy', 'idris', 2016]
    print("f(['lex', 'hy', 'idris', 2016]) = " + str(function(xUser)))