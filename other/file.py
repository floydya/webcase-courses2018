# 1 variant
with open("1.txt", "r") as f, open("g.txt", "w") as g: g.write(" ".join([x for x in f.read().replace("\n", " ").split(" ") if len(x) != 1 or len(x) != 2]))

# 2 variant
import re
with open("1.txt", "r") as f, open("g.txt", "w") as g: g.write(" ".join(re.findall(r"\w{3,}", f.read())))
