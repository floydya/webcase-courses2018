def checkio(words):
    counter = 0
    lst = words.split(' ')
    for i in range(0, len(lst)):
        if lst[i].isnumeric() == False:
            counter += 1
        if lst[i].isnumeric() and counter > 0:
            counter = 0
        if counter == 3:
            break
    return True if counter >= 3 else False
