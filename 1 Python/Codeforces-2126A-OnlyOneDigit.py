nc = int(input())

for _ in range(nc):
    #since we want to find a minima, we can approach using strings instead of ints
    numStr = str(input())
    print(sorted(numStr)[0])
