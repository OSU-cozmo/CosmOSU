def checkNegative(exp):
    s = exp.split()
    final = ""
    first = True
    for x in s:
        templ = len(x)
        if templ > 1 and x[1:].isnumeric() and x[0] == '-':
            x = 'negative ' + x[1:]
        if not first:
            x = " " + x
        final = final + x
        first = False
    return final
print(checkNegative("5 + -5 - 3"))
