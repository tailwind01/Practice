import sys
from collections import Counter

def solve():
    # Fast I/O: read all input at once or use readline
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        # Extract the current test case's array slice
        arr = input[ptr : ptr + n]
        ptr += n
        
        # Count frequencies in O(n)
        counts = Counter(arr)
        
        # Find any element with count >= 3
        found = -1
        for x, count in counts.items():
            if count >= 3:
                found = x
                break
        results.append(str(found))
    
    # Batch print for speed
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

##the code that failed on testcase 45 due to exceeding time limit is as follows which is commented..

#import statistics as s

#nc = int(input())

#for _ in range(nc):
#    l = int(input())
#    b = list(map(int, input().rstrip().split()))
#    maxAppearance = s.mode(b)
#    if b.count(maxAppearance)>=3:
#        print(maxAppearance)
    #else:
#        print(-1)
