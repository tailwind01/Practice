#storing in memory the levels for each number through 100 the sum in AP


memList = [i*(i+1)//2 for i in range(1,101)]
recursiveSum = [sum(memList[:i]) for i in range(len(memList))]

numCubes = int(input())


if numCubes==1:
    print(1)
else:
    for n in recursiveSum:
        if n<=numCubes:
            continue
        else:
            print(recursiveSum.index(n)-1)
            break
