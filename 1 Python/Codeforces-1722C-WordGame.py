nc = int(input())

for _ in range(nc):
    nw = int(input())
    p1 = list(map(str,input().rstrip().split()))
    p2 = list(map(str,input().rstrip().split()))
    p3 = list(map(str,input().rstrip().split()))
    p12 = len(set(p1).intersection(p2))
    p13 = len(set(p1).intersection(p3))
    p23 = len(set(p2).intersection(p3))
    p123 = len(set(p1).intersection(set(p2).intersection(p3)))
    points1 = max(0,nw-p12-p13+p123)*3+ p12*1 + p13*1 - p123*2
    points2 =  max(0,nw-p12-p23+p123)*3+ p12*1 + p23*1 - p123*2
    points3 = max(0,nw-p13-p23+p123)*3+ p13*1 + p23*1 - p123*2
    ans = [points1,points2, points3]
    print(*ans)
