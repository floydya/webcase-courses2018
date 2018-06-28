def checkio(data):
    newmas = []
    for x in data:
        if data.count(x) > 1:
            newmas.append(x)
    return newmas
