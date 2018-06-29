from optparse import OptionParser
import os, sys


parser = OptionParser()
parser.add_option("-H", "--hidden", action="store_false", help="show hidden files [default: off]")
parser.add_option("-m", "--modified", action="store_false", help="show last modified date/time [default: off]")
parser.add_option("-o", "--order", action="store", default='name', help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
parser.add_option("-r", "--recursive", action="store_false", help="recurse into subdirectories [default: off]")
parser.add_option("-s", "--sizes", action="store_false", help="show sizes [default: off]")


(options, args) = parser.parse_args()