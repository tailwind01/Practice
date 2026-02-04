nc = int(input())
x = 0
for _ in range(nc):
    n,s,m = map(int, input().rstrip().split())
    timePtr = 0
    bathBool = 0
    sfArr = []
    for x in range(n):
        sf = list(map (int, input().rstrip().split()))
        sfArr+=[sf]

    for t in sfArr:
        start = t[0]
        fin = t[1]
        if (start-timePtr)>=s: 
            bathBool=1
            break # as soon as we have found time, we get out of reading the input as we have found our answer
        else:
            timePtr = fin

    if (m-timePtr)>=s: # upon finishing the last task, do we have time?
        bathBool = 1

    print("Yes" if bathBool==1 else "No")
