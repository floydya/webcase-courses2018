def checkio(number):
    rslt = 1
    for i in str(number):
        if int(i) != 0:
            rslt *= int(i)
    return rslt
