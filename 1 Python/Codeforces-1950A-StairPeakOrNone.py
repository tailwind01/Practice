nc = int (input())

for _ in range(nc):
    a,b,c = map(int, input().rstrip().split())
    
    if a<b and b<c:
        print("STAIR")
    elif b>a and b>c:
        print("PEAK")
    else:
        print("NONE")
