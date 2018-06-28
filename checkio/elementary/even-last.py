def checkio(array):
    sum = 0
    if len(array) < 1:
        return 0
    for i in range(0, len(array)):
        if i % 2 == 0:
            sum += array[i]

    return sum * array[len(array)-1]
