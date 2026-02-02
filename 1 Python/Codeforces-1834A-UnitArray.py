#using mathematical intuition
t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    lp1 = l.count(1)
    lm1 = l.count(-1)
    operations = 0
    # sum is dependent on the relative counts: relative lp1>=lm1
    # product is dependent upon the even/odd count of -1s
    # we shall strive to first correct the sum 
    # the if conditions should be partially independent

    if(lm1>lp1):
        if (lm1-lp1)%2!=0:
            operations += (lm1+1-lp1)//2 # sum is corrected at each swap by 2 (1-(-1))
        else:
            operations += (lm1-lp1)//2 # sum is corrected at each swap by 2 (1-(-1))
        
    if (lm1-operations)%2!=0: # mindful of post-operations count of -1s
        operations+=1 # for correcting the products
    
    print(operations)

# using list traversal
t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    l.sort()
    operations = 0
    for i in range(n):
        if sum(l)<0 or l.count(-1)%2!=0:
            l[i] = 1
            operations+=1
        else:
            break
    print(operations)
