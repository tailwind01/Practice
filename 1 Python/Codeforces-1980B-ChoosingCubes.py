nc = int(input())

for _ in range(nc):
    n,f,k = map(int, input().rstrip().split())
    cubes = list(map(int, input().rstrip().split()))
    favorite = cubes[f-1]
    origFCt = cubes.count(favorite)
    afterK = sorted(cubes,reverse=True)[k:]
    ans = "Yes" if favorite not in afterK else "Maybe" if afterK.count(favorite)<origFCt else "No"
    print(ans)
