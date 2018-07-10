import re
import sys
import urllib.request as URLR

txt_regex = re.compile(r"<[^/!][^>]*?>")
tag_regex = re.compile(r"<(?P<tag>\w+)")
intag_regex = re.compile(r'(?P<key>\w+?)\s*=\s*(?P<value>"[^"]+"*)')
matches = []

if len(sys.argv) < 2:
    print("use: {} [URL]".format(sys.argv[0]))
else:
    lines = str(URLR.urlopen(sys.argv[1]).read())
    for match in txt_regex.findall(lines):
        matches.append(match)
    for tag in matches:
        try:
            tagg = tag_regex.match(tag)
            print(tagg.group("tag"))
            for i in intag_regex.findall(tag):
                print("\t" + str(i[0]) + "=" + str(i[1]))
        except AttributeError:
            continue
