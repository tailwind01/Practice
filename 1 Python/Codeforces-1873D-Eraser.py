t = int(input())

for _ in range(t):
    n,k = map(int, input().rstrip().split())
    istr = list(str(input()))
    ops = 0
    i = 0
    while i<n:
        if istr[i]=='B':
            ops+=1
            i = i+k
        else:
            i = i+1
    print(ops)
