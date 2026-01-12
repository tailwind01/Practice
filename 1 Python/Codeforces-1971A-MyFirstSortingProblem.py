nc = int(input())

for _ in range(nc):
    i = list(map(str, input().rstrip().split()))
    print(" ".join(sorted(i)))
