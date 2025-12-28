nc = int(input())

for _ in range(nc):
    distances = list(map(int, input().rstrip().split()))
    a = distances[0]
    sortedDistances = sorted(distances)[::-1] #sorted smallest to largest
    print(sortedDistances.index(a))

    
