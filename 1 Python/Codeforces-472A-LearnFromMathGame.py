import math as m

def isPrime(n):
    verdict = 1
    upperLimit = int(m.sqrt(n))+1
    for x in range(2,upperLimit):
        if n%x==0:
            verdict = 0
            break

    return 1==1 if verdict==1 else 1==0

def primes():
    primesList = [2,3]
    for x in range(4,1000001):
        if isPrime(x):
            primesList.append(x)   
    return primesList

primeNumbers=primes()
number = int(input())

for n in range(number-2,number//2,-1):
    if n not in primeNumbers and (number-n) not in primeNumbers:
        print(str(n)+" "+str(number-n))
        break




