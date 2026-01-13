import sys

def legs():
    t = int(input())
    results = []
    
    for i in range(t):
        n = int(input())
        if n>4:
            ans = n//4
        
            if n%4!=0: ans+=1 #we have additional legs present, so they are of a chick!
        else:
            ans = 1

        results.append(str(ans))
    
    sys.stdout.write('\n'.join(results) + '\n')

legs()
