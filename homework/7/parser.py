import re, sys

txt_regex = re.compile(r"<[^/!][^>]*?>")
tag_regex = re.compile(r"<(?P<tag>\w+)")
intag_regex = re.compile(r'(?P<key>\w+?)\s*=\s*(?P<value>"[^"]+"*)')
matches = []
tags = dict()


if len(sys.argv) < 2:
    print("use: {} [fileNAME]".format(sys.argv[0]))
else:
    try:
        file = open(sys.argv[1])
        lines = file.read()
        for match in txt_regex.findall(lines):
            matches.append(match)
        for tag in matches:
            dictionary = dict()
            for i in intag_regex.findall(tag):
                dictionary[i[0]] = i[1]
            tags[tag_regex.match(tag).group(1)] = dictionary
    except Exception as err:
        print(err)
    finally:
        file.close()

for key, value in tags.items():
    print(key)
    for k, v in value.items():
        print("\t{} = {}".format(k, v))
