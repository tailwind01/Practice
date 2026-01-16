nc = int(input())

for _ in range(nc):
    n,a,b = map(int,input().rstrip().split())
    
    if b>2*a:
        print(n*a)
    elif n%2==1:
        print((n-1)//2 * b + a)
    else:
        print((n//2)*b)
