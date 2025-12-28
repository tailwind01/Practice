nc = int(input())

for _ in range(nc):
    a,b,c = map(int, input().rstrip().split())
    if a+b==c:
        print("+")
    else:
        print("-")
    
