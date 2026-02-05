nc = int(input())

for _ in range(nc):
    a,b,c,d = map(int, input().rstrip().split())
    vert = d-b
    horiz = c-a

    if horiz>vert or vert < 0:
        ans = -1
    else:
        ans = 2*vert - horiz

    print(ans)
