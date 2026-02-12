nc = int(input())

# hyp is that because every integer has a square, every integer is a perfect root!
for _ in range(nc):
    n = int(input())
    ansRange = list(range(1,n+1,1))
    print(*ansRange)
