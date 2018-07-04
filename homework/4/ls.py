from optparse import OptionParser
import os, sys, datetime


parser = OptionParser()
parser.add_option("-H", "--hidden", action="store_true", dest="hidden", help="show hidden files [default: off]")
parser.add_option("-m", "--modified", dest="modified", action="store_true", help="show last modified date/time [default: off]")
parser.add_option("-o", "--order", dest="order", type="str", help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
parser.add_option("-r", "--recursive", dest="recursive", action="store_true", help="recurse into subdirectories [default: off]")
parser.add_option("-s", "--sizes", dest="sizes", action="store_true", help="show sizes [default: off]")
parser.set_defaults(order='name')

(options, args) = parser.parse_args()
args = "." if not args else args[0]
dirs = []
the_best_of_the_best = []

# ([name, size, date], [name, size, date])
# for i in tuple:
#     name = i[0]
#     size = i[1]
#     date = i[2]


if not options.recursive:
    with os.scandir(".") as it:
        for entry in it:
            if not options.hidden and entry.name.startswith("."):
                continue
            the_best_of_the_best.append([entry.name, os.stat(entry.name).st_size, datetime.datetime.fromtimestamp(os.path.getmtime(entry.name)).strftime("%Y-%m-%d %H-%M-%S")])
else:
    dirs = os.walk(args)
    for obj in dirs:
        for i in obj[2]:
            the_best_of_the_best.append(["{}/{}".format(obj[0], i).replace("\\", "/"), 
                                        os.stat("{}/{}".format(obj[0], i).replace("\\", "/")).st_size,
                                        datetime.datetime.fromtimestamp(os.path.getmtime("{}/{}".format(obj[0], i).replace("\\", "/"))).strftime("%Y-%m-%d %H-%M-%S")])
    
def print_list(dirs_list, order, modified=False, sizes=False):
    if order in ('name', 'n', 'modified', 'm', 'size', 's'):
        if order in ('name', 'n'):
            order_by = lambda x: x[0]
        elif order in ('size', 's'):
            order_by = lambda x: x[1]
        else:
            order_by = lambda x: x[2]
    else:
        order_by = lambda x: x[0]
    for item in sorted(dirs_list, key=order_by):
        line = ""
        if modified:
            line += str(item[2]) + "\t"
        if sizes:
            line += str(item[1]) + "\t"
        line += item[0]
        print(line)

print_list(the_best_of_the_best, options.order, options.modified, options.sizes)