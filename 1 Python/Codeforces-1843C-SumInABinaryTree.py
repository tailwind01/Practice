nc = int(input())

for _ in range(nc):
    n = int(input())
    cumsum = 0
    while n>0:
        cumsum+=n
        n=n//2
    print(cumsum)
