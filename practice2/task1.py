def function(x):
    output = -1
    if x[0] == "tea":
        if x[4] == "2010":
            if x[1] == "2000":
                output = 0
            elif x[1] == "1996":
                output = 1
            elif x[1] == "2014":
                if x[3] == "vue":
                    output = 2
                elif x[3] == "numpy":
                    output = 3
        elif x[4] == "1980":
            if x[3] == "vue":
                output = 4
            elif x[3] == "numpy":
                if x[1] == "2000":
                    output = 5
                elif x[1] == "1996":
                    output = 6
                elif x[1] == "2014":
                    output = 7
        elif x[4] == "1992":
            output = 8
    elif x[0] == "m4":
        output = 9
    elif x[0] == "csv":
        output = 10
    return output


if __name__ == '__main__':
    xUser = [str, str, str, str, str]
    for i in range(5):
        xUser[i] = input()
    print(str(function(xUser)))
