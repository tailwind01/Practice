nc = int(input())

for _ in range(nc):
    n,m = map(int, input().rstrip().split())
    first_space = m
    accomodated = 0
    for i in range(n):
        s_word = str(input())
        s_size = len(s_word)
        first_space-=s_size
        if first_space>=0:
            accomodated+=1

    print(accomodated)
