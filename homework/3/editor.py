import os, sys


def main():
    lst = [file for file in os.listdir(path=".") if '.lst' in file]
    if lst:
        print('Available .lst files:')
        for index, name in enumerate(lst, 1):
            print('{}. {}'.format(index, name))
        while True:
            try:
                choosen = int(input('Choose file index from list above(1-{}) or 0 to create new: '.format(len(lst))))
                break
            except ValueError:
                print('Try enter number(1-{}) or ZERO to create new file.'.format(len(lst)))
        if choosen:
            process_file(lst[choosen-1])
        else:
            filename = input('Enter file name here: ')
            if filename in os.listdir(path="."):
                arr = []
                with open(filename) as file:
                    for line in file:
                        arr.append(line.strip())
                process_file(arr)
            else:
                f = open(filename,"w+")
                f.close()
                arr = []
                process_file(arr, empty=True)


def process_file(array, empty=False):
    if empty:
        print("-- no items in the list --")
        while True:
            action = input('[A]dd [Q]uit [a/q]: ')
            if action in ('AaQq'):
                func = action
                break
            else:
                print('Error: invalid action -> enter one of "AaQq"')
    if not empty:
        for index, line in enumerate(array, 1):
            print('{}. {}'.format(index, line))
        while True:
            action = input('[A]dd [D]elete [S]ave [Q]uit [a/d/s/q]: ')
            if action in ('AaDdSsQq'):
                func = action
                break
            else:
                print('Error: invalid action -> enter one of "AaDdSsQq"')
    func(func, array)


def func(action, array):
    if action in 'Aa':
        input('Enter new line: ')
    elif action in 'Dd':
        print('del')
    elif action in 'Ss':
        print('save')
        file.flush()
    else:
        print('close')
        file.close()
        sys.exit()

main()