
nc = int(input())

for _ in range(nc):
    n = int(input())
    a = list(map(int, input().split()))
    setA = set(a)
    
    if len(setA)==1:
        print(0)
    else:
        print(sum(a)-n*min(a))
