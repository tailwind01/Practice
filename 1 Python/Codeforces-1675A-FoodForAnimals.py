nc = int(input())

for _ in range(nc):
    a,b,c,x,y = map(int, input().rstrip().split())
    cats = max(x-a,0)
    dogs = max(y-b,0)
    ans =  "Yes" if c-cats-dogs>=0 else "No" # we use the common food only to feed shortage
    print(ans)
