def checkio(*args):
    lst = []
    if args:
        for x in args:
            lst.append(x)
        return max(lst)-min(lst)
    else:
        return 0
