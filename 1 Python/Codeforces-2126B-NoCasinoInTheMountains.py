tc = int(input())

for _ in range(tc):
    n,k = map(int, input().rstrip().split())
    wc = list(map(int, input().rstrip().split()))
    hikes = 0
    zeroColl = 0
    for i in wc:
        if i==0:
            zeroColl+=1
            if zeroColl==k:
                hikes+=1
                zeroColl = -1 #hyp for the restday
        else:
            zeroColl = 0
    print(hikes)
