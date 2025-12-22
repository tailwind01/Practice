    import bisect as b
     
    nc = int(input())
     
    ansArr = []
    for c in range(nc):
        elems = int(input())
        iL = list(map(int,input().rstrip().split()))
        loopL = []
        for e in iL:
            if e not in loopL:
                b.insort_left(loopL, e)
        difAr = []        
        for l in range(len(loopL)-1):
            consDif = loopL[l+1] - loopL[l]
            difAr+=[consDif]
        
        if len(difAr)>=1:
            maxDiff = max(difAr)
        else:
            maxDiff = 0
        
        if maxDiff>1:
            ansArr+=["NO"]
        else:
            ansArr+=['YES']
     
     
    print("\n".join(ansArr))


#link for testcases and full solution https://codeforces.com/contest/1399/submission/118131772



