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
                process_file(filename)
            else:
                process_file(filename, empty=True)


def process_file(filename, empty=False):
    if empty:
        f = open(filename,"c")
        f.close()
        print("-- no items in the list --")
        while True:
            action = input('[A]dd [Q]uit [a/q]: ')
            if action in ('AaQq'):
                func = action
                break
            else:
                print('Error: invalid action -> enter one of "AaQq"')
    if not empty:
        for index, line in enumerate(file, 1):
            print('{}. {}'.format(index, line.strip()))
        while True:
            action = input('[A]dd [D]elete [S]ave [Q]uit [a/d/s/q]: ')
            if action in ('AaDdSsQq'):
                func = action
                break
            else:
                print('Error: invalid action -> enter one of "AaDdSsQq"')
    file = open(filename,"r+")
    func(func, file)


def func(action, file):
    if action in 'Aa':
        input('Enter new line: ')
    elif action in 'Dd':
        pass
    elif action in 'Ss':
        file.flush()
    else:
        file.close()
        sys.exit()

main()