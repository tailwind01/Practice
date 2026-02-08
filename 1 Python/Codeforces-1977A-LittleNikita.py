nc = int(input())

for _ in range(nc):
    n,m = map(int, input().rstrip().split())
    ansBool = 1 # lets assume we can always find an answer, which will change if we cant

    # condition 1 : n is strictly less than m..
    if n<m:
        ansBool = 0
    # condition 2 : the absence of even parity even if m is less than n..
    elif (n-m)%2!=0:
        ansBool = 0

    print("Yes" if ansBool==1 else "No")
