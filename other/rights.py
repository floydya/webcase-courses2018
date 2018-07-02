from collections import defaultdict

rights = defaultdict(set)


for i in range(int(input())):
	line = input().split(' ')
	if len(line) > 1:
		rights[line[0]] = set(line[1:len(line)])
	else:
		rights[line[0]] = set()


exit = []


for i in range(int(input())):
	line = input().split(' ')
	if line[0] == 'read':
		if 'R' in rights[line[1]]:
			 exit.append('OK')
		else:
			exit.append('Access denied')
	elif line[0] == 'write':
		if 'W' in rights[line[1]]:
			exit.append('OK')
		else:
			exit.append('Access denied')
	elif line[0] == 'execute':
		if 'X' in rights[line[1]]:
			exit.append('OK')
		else:
			exit.append('Access denied')
	else:
		exit.append('Error')


print(*exit, sep='\n')
