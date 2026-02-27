# forward pass version
nc = int(input())

for _ in range(nc):
    n = int(input())
    wa = list(map(int, input().rstrip().split()))
    target = sum(wa)//n
    collectedfromleft = 0
    ansBool  = 1
    for i in range(n-1,-1,-1):
        collectedfromleft+=target-wa[i]
        if collectedfromleft<0:
            ansBool = 0
            break
    print("Yes" if ansBool==1 else "No")

# backward pass version
nc = int(input())

for _ in range(nc):
    n = int(input())
    wa = list(map(int, input().rstrip().split()))
    target = sum(wa)//n
    requiredFromLeft = 0
    ansBool  = 1
    for i in range(n-1,-1,-1):
        requiredFromLeft+=target-wa[i]
        if requiredFromLeft<0:
            ansBool = 0
            break
    print("Yes" if ansBool==1 else "No")
