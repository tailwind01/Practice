nc = int(input())

for _ in range(nc):
    n = int(input())
    m7 = n%7
    ans = n-m7 if n//10==(n-m7)//10 else n+7-m7
    print(ans)
