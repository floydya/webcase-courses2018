import os, sys

"""
if len(sys.argv) < 2:
    path = ["."]
    key = None
elif len(sys.argv) == 2:
    path = ["."]
    key = sys.argv[1]
elif len(sys.argv) > 2:
    path = sys.argv[2:]
    key = sys.argv[1]
"""
keys = []
path = []
if len(sys.argv) > 1:
    for key in sys.argv[1:]:
        if '-' in key:
            keys.append(key)
        else:
            if os.path.exists(key):
                path.append(key)

if '-h' in keys or '--help' in keys:
    print('Usage: {} [options] [path1 [path2 [ ... pathN]]]\n'.format(sys.argv[0]))
    print('The paths are optional; if not given . is used.\n')
    print('Options:')
    print('\t-h, --help\tshow this help message and exit')
    print('\t-H, --hidden\tshow hidden files [default: off]')
    print('\t-m, --modified\tshow last midified date/time [default:off]')
    print('\t-o ORDER, --order=ORDER')
    print("\t\t\torder by ('name', 'n', 'modified', 'm', 'size', 's')\n\t\t\t[default: name]")
    print('\t-r, --recursive\trecurse into subdirectories [default: off]')
    print('\t-s, --sizes\tshow sizes [default: off]')
