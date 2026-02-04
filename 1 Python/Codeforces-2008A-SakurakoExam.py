t = int(input())

for _ in range(t):
    a,b = map(int, input().rstrip().split())
    if (a==0 and b%2!=0) or (b==0 and a%2!=0) or (b%2!=0 and a%2!=0):
        print("NO")
    else:
        if (a+2*b)%2!=0:
            print("NO")
        else:
            print("YES")
