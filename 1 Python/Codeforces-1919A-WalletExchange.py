tc = int(input())

for _ in range(tc):
    a,b = map(int,input().rstrip().split())
    ans = "Bob" if (a+b)%2==0 else "Alice"
    print(ans)
