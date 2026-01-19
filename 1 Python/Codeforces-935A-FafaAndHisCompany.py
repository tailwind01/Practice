#v2 - using a primes sieve approach
import math as m
LIMIT = 32000
primes = []
is_prime = [True] * (LIMIT + 1)
for p in range(2, LIMIT + 1):
    if is_prime[p]:
        primes.append(p)
        for i in range(p * p, LIMIT + 1, p):
            is_prime[i] = False

def solve():
    n = int(input())
    temp = n
    total_divisors = 1 
    for p in primes:
        if p * p > temp:
            break
        if temp % p == 0:
            exponent = 0
            while temp % p == 0:
                exponent += 1
                temp //= p
            total_divisors *= (exponent + 1)
            
    if temp > 1:
        total_divisors *= 2
        
    print(total_divisors - 1)

solve()
################============================================#######################
# v1
n = int(input())
ans = 1
for x in range(2,n//2+1):
    if n%x==0:
        ans+=1

print(ans)
