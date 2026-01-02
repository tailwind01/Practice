t = int(input())

for _ in range(t):
	n = int(input())
	iterlist = list(map(int, input().rstrip().split()))
	firstElem = iterlist[0]
	outputlist = [firstElem]
	for x in range(1,n):
		if iterlist[x]<=firstElem:
			outputlist.append(firstElem)
		else:
			outputlist.append(iterlist[x])
	
	print(*outputlist)
