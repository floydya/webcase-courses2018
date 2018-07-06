import re


tel_re = r"""(
             \d{3}                  # 3 nums
             [\s]??                 # tabs\spaces\newlines
             \d{3}                  # 3 nums
             [\s]??                 # tabs\spaces\newlines
             \d{4}                  # 4 nums
             |                      # --------------or---------------
             \(\d{3}\)              # (nnn) where n = number(0-9)
             \s*                    # tabs\spaces\newlines or nothing
             \d{3}                  # 3 nums
             [\s]??                 # tabs\spaces\newlines
             \d{4}                  # 4 nums
             )
"""
regexp_tel = re.compile(tel_re, re.VERBOSE)

line = input("Enter number or leave empty for exit: ")
assert regexp_tel.match(line), "unsupported format of telephone number"

for symbol in (' ', '(', ')', '\t', '\n'):
    line = line.replace(symbol, '')
print("({0}) {1} {2}".format(line[:3], line[3:6], line[6:]))