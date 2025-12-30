nc = int(input())

for _ in range(nc):
    numList = list(map(int, input().rstrip().split()))
    sortedNumList = sorted(numList)
    print(sortedNumList[1])
