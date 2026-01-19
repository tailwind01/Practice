# 3 versions - 1 O(n+m), 2 O(nm)
# these 3 are separate chunks of the code, all of which solve the problem
# it must however be kept in mind not to run all 3 in one interpreter :D
# v3 - final version - optimized code
nc = int(input())

for _ in range(nc):
    n,m,k = map(int, input().rstrip().split())
    nPock = sorted(list(map(int, input().rstrip().split())))
    mPock = sorted(list(map(int, input().rstrip().split())))
    # O(n + m) approach after sorting
    count = 0
    left = 0
    right = m - 1

    while left < n and right >= 0: #we traverse from both ends
        if nPock[left] + mPock[right] <= k:
        # If this pair works, then nPock[left] works with 
        # EVERY element in mPock from index 0 to 'right'
            count += (right + 1)
            left += 1
        else:
        # Sum is too large, make the sum smaller by moving the right pointer
        #let's come behind a little
            right -= 1
        
    print(count)

# v2 - bruteforce without any reduction

nc = int(input())

for _ in range(nc):
    n,m,k = map(int, input().rstrip().split())
    nPock = sorted(list(map(int, input().rstrip().split())))
    mPock = sorted(list(map(int, input().rstrip().split())))
    
    ctrList = [1 if x + y <= k else 0 for x in nPock for y in mPock]
    
    print(sum(ctrList))

# v1 : reduction done using bisect and then only comparisons start

import bisect as b
nc = int(input())

for _ in range(nc):
    n,m,k = map(int, input().rstrip().split())
    nPock = sorted(list(map(int, input().rstrip().split())))
    mPock = sorted(list(map(int, input().rstrip().split())))
    #we have to select one coin from each pocket, so strict condition is there
    nSize = b.bisect_left(nPock,k)
    mSize = b.bisect_left(mPock,k)
    reducedN = nPock[:nSize]
    reducedM = mPock[:mSize]
    
    count = 0
    
    for i in range(len(reducedN)):
        nElem = reducedN[i]
        for j in range(len(reducedM)):
            mElem = reducedM[j]
            if nElem+mElem<=k:
                count+=1
    
    print(count)
