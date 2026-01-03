nc = int(input())
     
for _ in range(nc):
    n,x = map(int, input().rstrip().split())
    inputList = list(map(int,input().rstrip().split()))
    print ("YES" if x in inputList else "NO")

