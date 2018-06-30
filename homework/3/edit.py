from os import listdir
import sys

lst_files_in_dir = [x for x in listdir('.') if '.lst' in x]
selected_file = str()
file_lines = list()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                        name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                                 "{minimum_length} and at most "
                                 "{maximum_length} characters".format(
                    **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):
    class RangeError(Exception):
        pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                                 "and {maximum} inclusive{0}".format(
                    " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


def create_new_file():
    filename = get_string("Enter name for new file") + ".lst"
    open(filename, "w+").close()
    return filename


def open_file(filename):
    array = []
    with open(filename, "r") as file:
        for line in file.readlines():
            array.append(line.strip())
    return array


def edit_file(file_lines_array):
    if not file_lines_array:
        print("-- no items in the list --")
        what_to_do = get_string("[A]dd [Q]uit [empty line = a]", default="a")
    else:
        for line_id, line in enumerate(file_lines_array, 1):
            print("{}. {}".format(line_id, line))
        what_to_do = get_string("[A]dd [D]elete [S]ave [Q]uit [empty line = a]", default="a")
    return what_to_do


def process_action(action, file_lines_array, filename):
    if action in 'Aa':
        file_lines_array.append(get_string("Add item"))
    elif action in 'Dd':
        if file_lines_array:
            to_delete_id = get_integer("Delete item number (or 0 to cancel)", minimum=1, maximum=len(file_lines_array))
            if to_delete_id:
                del file_lines_array[to_delete_id-1]
            else:
                return
        else:
            return
    elif action in 'Ss':
        if not check_file_status(filename, file_lines_array):
            if get_string("Save unsaved changes (y/n) [y]", default='Y') in 'Yy':
                with open(filename, "w+") as file:
                    file.truncate()
                    file.writelines("%s\n" % l for l in file_lines_array)
        else:
            print("~~~[INFO] Nothing to save")
    elif action in 'Qq':
        if not check_file_status(filename, file_lines_array):
            process_action('s', file_lines_array, filename)
            sys.exit()


def check_file_status(filename, file_lines_array):
    array = []
    with open(filename, "r") as file:
        for line in file.readlines():
            array.append(line)
    if array == file_lines_array:
        return True
    return False


if not lst_files_in_dir:
    selected_file = create_new_file()
else:
    for index, name in enumerate(lst_files_in_dir, 1):
        print("{}. {}".format(index, name))
    file_id = get_integer("Enter file ID(1 - {}) to edit or 0 to"
                          "create new".format(len(lst_files_in_dir)),
                          minimum=1, maximum=len(lst_files_in_dir))
    if not file_id:
        selected_file = create_new_file()
    else:
        selected_file = lst_files_in_dir[file_id - 1]

file_lines = open_file(selected_file)

while True:
    process_action(edit_file(file_lines), file_lines, selected_file)
