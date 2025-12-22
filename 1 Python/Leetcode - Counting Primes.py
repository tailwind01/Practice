import math
N = 5000005
dp = [0] * (N + 1)
def sieve():
    array = [0] * (N + 1)
    array[0] = 1
    array[1] = 1
    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if array[i] == 0:
            for j in range(i * i, N + 1, i):
                array[j] = 1
    
    for i in range(1, N + 1):
        if array[i] == 0:
            dp[i] = 1
        
sieve()

class Solution:
    def countPrimes(self, n: int) -> int:
        #instead of calling the sieve inside the loop, create a copy of sieve in the memory itself
        return sum(dp[:n])
