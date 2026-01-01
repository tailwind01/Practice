n,m = map(int, input().rstrip().split())
setTraversal = list(map(int, input().rstrip().split()))
A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))
happiness = 0 #starts at 0

for i in setTraversal:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
    else:
        happiness = happiness

print(happiness)
