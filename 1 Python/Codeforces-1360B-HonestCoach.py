nc=int(input())

for _ in range(nc):
    n = int(input())
    stArr = list(map(int, input().rstrip().split()))
    stArr_s = sorted(stArr)
    minDiff = abs(stArr_s[0]-stArr_s[1]) # initialized as there has to be at least 1 player in each team
    
    for i in range(2,n):
        if abs(stArr_s[i]-stArr_s[i-1])<minDiff:
            minDiff = abs(stArr_s[i]-stArr_s[i-1])
    
    print(minDiff)
