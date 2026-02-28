nc = int(input())

for _ in range(nc):
    d = int(input())
    mc = list(map(int, input().rstrip().split()))
    sc = list(map(int, input().rstrip().split()))
    lead = mc[d-1]
    if d>1:
        for i in range(d-2,-1,-1):
            if mc[i]>sc[i+1]:
                lead+=mc[i]-sc[i+1]
    print(lead)
