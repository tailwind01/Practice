nc = int(input())

#without overcomplicating stuff, we can go for the killshot of making all sums equal
for _ in range(nc):
    n = int(input())
    il = list(map(int, input().rstrip().split()))
    ansArr = [n+1-i for i in il]
    print(*ansArr)
