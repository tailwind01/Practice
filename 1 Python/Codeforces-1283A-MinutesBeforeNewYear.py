nc = int(input())

for _ in range(nc):
    hhmm = list(map(int, input().rstrip().split()))
    
    print(24*60-(hhmm[0]*60+hhmm[1]))
