##v2
nc = int(input())

for _ in range(nc):
    n = int(input())
    digits = list(map(int,input().rstrip().split()))
    requirements = [3,1,2,1,0,1] # value 0 assigned to 4 so that it doesnt bother us
    uniques = 5 #(0,1,2,3,5)
    ans = 0 # we change this only if we see evidence otherwise
    for i,num in enumerate(digits):
        if num<6 and uniques>0:
            requirements[num]-=1
            if requirements[num]==0:
                uniques-=1
        if uniques==0:
            ans = i+1
            break

    print(ans)


## v1
nc = int(input())

for _ in range(nc):
    n = int(input())
    digits = list(map(int,input().rstrip().split()))
    ct0 = 3
    ct1 = 1
    ct2 = 2
    ct3 = 1
    ct5 = 1
    ans = 0 # we change this only if the array meets conditions
    for x in range(n):
        num = digits[x]
        if num==0:
                ct0-=1
        elif num==1:
            ct1-=1
        elif num==2:
            ct2-=1
        elif num==3:
            ct3-=1
        elif num==5:
            ct5-=1
        if ct0 <= 0 and ct1<=0 and ct2<=0 and ct3<=0 and ct5<=0:
            ans = x+1
            break
    print(ans)
