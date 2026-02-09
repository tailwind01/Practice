nc = int(input())

for _ in range(nc):
    a,b,c = map(int, input().rstrip().split())
    diff = abs(b-a)
    ceiling = 2*diff
    # if we already have an invalid state, we discard
    if a>ceiling or b>ceiling or c>ceiling or diff==1:
        ans = -1
    else:
        if c+diff>ceiling:
            ans = c-diff
        else:
            ans = c+diff
    print(ans)
