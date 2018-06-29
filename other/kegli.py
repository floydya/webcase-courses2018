N = ["I" for i in range(int(input()))]
K = int(input())
arr = []


for i in range(K):
	arr += [int(i) for i in input().split()]


for index in range(1, len(N)+1):
	if index in set(arr): 
		N[index-1] = "."


print(*N)

