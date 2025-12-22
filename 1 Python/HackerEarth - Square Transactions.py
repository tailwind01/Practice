#/ a tailwind code, smooth run 1.1s, 8Mbs
import bisect as b
numtr = int(input())
valarr = list(map(int, input().rstrip().split()))
cumsum = [0]
for v in valarr:
    cumsum+=[cumsum[-1]+v]

nq = int(input())

for q in range(nq):
    tgt = int(input())
    ansind = b.bisect(cumsum,tgt)
    if ansind==numtr+1 and cumsum[-1]!=tgt:
        print(-1)
    else:
        if(cumsum[ansind-1]==tgt):
            print(ansind-1)
        else:
            print(ansind)
