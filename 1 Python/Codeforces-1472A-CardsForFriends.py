nc = int(input())

for _ in range(nc):
    w, h, n = map(int, input().rstrip().split())
    total_cards = 1
    while w % 2 == 0:
        w //= 2
        total_cards *= 2
    while h % 2 == 0:
        h //= 2
        total_cards *= 2
    if total_cards >= n:
        print("YES")
    else:
        print("NO")
