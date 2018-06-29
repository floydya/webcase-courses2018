dictionary = dict()

for i in range(int(input())):
	string = input().split()
	dictionary[string[0]] = string[1]
	dictionary[string[1]] = string[0]

print(dictionary[input()])
