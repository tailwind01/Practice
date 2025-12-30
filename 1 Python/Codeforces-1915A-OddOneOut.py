nc = int(input())

for _ in range(nc):
    numList = list(map(int, input().rstrip().split()))
    ctList = [numList.count(i) for i in numList]
    print(numList[ctList.index(1)])
