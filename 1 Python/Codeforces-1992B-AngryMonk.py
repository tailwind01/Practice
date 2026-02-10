# generalized formula..
nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    pieces = list(map(int, input().rstrip().split()))
    print(2*(sum(pieces)-max(pieces))-(k-1))

# using list comprehension - the formula expanded..
#
nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    pieces = list(map(int, input().rstrip().split()))
    m1Arr = sum(sorted([2*(i-1)+1 for i in pieces], reverse=True)[1:])
    print(m1Arr)
