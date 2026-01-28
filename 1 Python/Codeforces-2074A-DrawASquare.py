tc = int(input())

for _ in range(tc):
    flag = 1 # we assume a square until we are proven otherwise
    v = list(map(int, input().rstrip().split()))
    for x in range(3):
        if v[x]!=v[x+1]:
            flag = 0
            break
    
    print("YES" if flag == 1 else "NO")
