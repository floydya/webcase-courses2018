from math import ceil, floor
lst = []
sorted_lst = []

while True:
    try:
        line = input('enter a number or Enter to finish:')
        if line:
            lst.append(int(line))
        else:
            break
    except ValueError as err:
        print(err)


try:
    while len(lst) > 0:
        sorted_lst.append(min(lst))
        lst.remove(min(lst))
    print('numbers:', sorted_lst)
    median = sorted_lst[(len(sorted_lst) - 1) // 2] if len(sorted_lst) % 2 else (sorted_lst[(len(sorted_lst) - 1) // 2] + sorted_lst[(len(sorted_lst) - 1) // 2 + 1])/2.0
    print('count = {} sum = {} lowest = {} highest = {} mean = {} median = {}'.format(len(sorted_lst), sum(sorted_lst), min(sorted_lst), max(sorted_lst), sum(sorted_lst) / float(len(sorted_lst)), median))
except ValueError:
    print('empty list')
