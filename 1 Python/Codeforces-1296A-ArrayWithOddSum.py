nc = int(input())

for _ in range(nc):
    size = int(input())
    cL = list(map(int, input().rstrip().split()))
    oddsbool = [1 if x%2!=0 else 0 for x in cL]
    oddsCt = sum(oddsbool)
    evenCt = size-oddsCt
    
    if (oddsCt>0 and evenCt>0) or oddsCt%2!=0:
        print("Yes")
    else:
        print("No")
