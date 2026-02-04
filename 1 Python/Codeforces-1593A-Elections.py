nc = int(input())

for _ in range(nc):
    abc = list(map(int, input().rstrip().split()))
    s_abc = sorted(set(abc))
    ansArr = []
    if len(s_abc) != 1:
        for e in abc:
            if e!=s_abc[-1]:
                ansArr.append(s_abc[-1]-e+1)
            else:
                if e==s_abc[-1] and abc.count(e)==2: # count of max element is 2 
                    ansArr.append(1)
                else:
                    ansArr.append(0)
    else: #trivial case..
        ansArr = [1,1,1]

    print(*ansArr)
