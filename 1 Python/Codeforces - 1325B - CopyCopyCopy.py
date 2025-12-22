#/tailwind code


nc = int(input())

for _ in range(nc):
    s = int(input())
    raw_l = list(map(int, input().rstrip().split()))
    print(len(set(raw_l)))
