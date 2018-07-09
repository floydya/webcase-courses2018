import re, sys

txt_regex = re.compile(r"<[^/!][^>]*?>")
tag_regex = re.compile(r"<(?P<tag>\w+)")
intag_regex = re.compile(r'(?P<key>\w+?)\s*=\s*(?P<value>"[^"]+"*)')
matches = []

if len(sys.argv) < 2:
	print("use: {} [fileNAME]".format(sys.argv[0]))
else:
	try:
		file = open(sys.argv[1])
		lines = file.read()
		for match in txt_regex.findall(lines):
			matches.append(match)
		for tag in matches:
			tagg = tag_regex.match(tag)
			print(tagg.group("tag"))
			for i in intag_regex.findall(tag):
				print("\t" + str(i[0]) + "=" + str(i[1]))
	except Exception as err:
		print(err)
	finally:
		file.close()
