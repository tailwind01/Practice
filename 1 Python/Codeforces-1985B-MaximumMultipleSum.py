import sys

def maxMultipleSums():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        if n==3:
            ans = 3
        else:
            ans = 2 #as 2 will have maximum number of multiples from 4 onwards to sum over

        results.append(str(ans))
    
    sys.stdout.write('\n'.join(results) + '\n')

maxMultipleSums()
