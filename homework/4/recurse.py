hidden = False
import os
paths = []
dirs = os.walk("..")
for obj in dirs:
    print(obj)
    for i in obj:
        if not hidden and 
    for i in obj[2]:
        paths.append("{}/{}".format(obj[0], i).replace("\\", "/"))

print(paths)
