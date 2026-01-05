n,m = map(int, input().rstrip().split())

primesTo50 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59] #manually passing in memory all the primes till 50 and some more to have runway for edge cases

nInd = primesTo50.index(n)

if m==primesTo50[nInd+1]:
    print("YES")
else:
    print("NO")
