#/tailwind 77ms,0k
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

n1, n2 = map(int, input().rstrip().split())

print(factorial(min(n1,n2)))
