nc = int(input())

for _ in range(nc):
    a,b = map(int, input().rstrip().split())
    print(a^b)
