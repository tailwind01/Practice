from collections import Counter as ctr
nc = int(input())

for _ in range(nc):
    s = str(input())
    ctrS = ctr(s)
    aCt = ctrS['A']
    bCt = ctrS['B']
    cCt = ctrS['C']
    # the hypothesis of this implementation is that count of B should be = A count+C count
    print("YES" if aCt+cCt-bCt==0 else "NO")
