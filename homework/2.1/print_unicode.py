import sys, unicodedata


def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        for word in words:
            if word in name.lower():
                print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                      code, name.title()))
        code += 1

words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [word1] [word2] [etc]".format(sys.argv[0]))
        words = []
    else:
        words = [x.lower() for x in sys.argv[1:]]
if len(words) > 0:
    print_unicode_table(words)
