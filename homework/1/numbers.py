lst = []


while True:
    try:
        line = input('enter a number or Enter to finish:')
        if line:
            lst.append(int(line))
        else:
            break
    except ValueError as err:
        print(err)


print('numbers:', lst)


try:
    print('count = {} sum = {} lowest = {} highest = {} mean = {}'.format(len(lst), sum(lst), min(lst), max(lst), sum(lst) / float(len(lst))))
except ValueError:
    print('empty list')
