nc = int(input())

for _ in range(nc):
    numList = list(map(int, input().rstrip().split()))
    maxNum = max(numList)
    minNum = min(numList)
    for n in numList:
        if n!=maxNum and n!=minNum:
            print(n)
    
