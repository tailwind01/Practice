    nc = int(input())
    for _ in range(nc):
        ar = list(map(int, input().rstrip().split()))
        sa1 = ar[:2]
        sa2 = ar[2:]
        sa1.sort()
        sa2.sort()
        sa1 = sa1[::-1]
        sa2 = sa2[::-1]
        if(sa1[0]<sa2[1] or sa2[0]<sa1[1]):
            print("NO")
        else:
            print("YES")