import string

is_ascii = lambda charstring: all(ord(c) < 128 for c in charstring)
is_ascii_punctuation = lambda charstring: set(charstring) <= set(string.punctuation)
is_ascii_printable = lambda charstring: set(charstring) <= set(string.printable)

print(is_ascii("ahsjkdhjashd"))
print(is_ascii("фыв"))
print(is_ascii_punctuation(",.!"))
print(is_ascii_punctuation("vosklitsatelniy znak!"))
print(is_ascii_printable("printable!\n"))
print(is_ascii_printable("unprintable!\b"))
