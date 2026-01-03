nc = int(input())

for _ in range(nc):
    l = int(input())
    iteredList = list(map(int, input().rstrip().split()))
    if sum(iteredList)%2==0:
        print("YES")
    else:
        print("NO")
