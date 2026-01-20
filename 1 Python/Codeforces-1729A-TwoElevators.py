nc = int(input())

for _ in range(nc):
    a,b,c = map(int, input().rstrip().split())
    ansArr = [a-1, abs(c-b)+abs(c-1)]
    
    ans = 3
    if ansArr[0]>ansArr[1]:
        ans = 2
    elif ansArr[0]<ansArr[1]:
        ans = 1
    
    print(ans)
