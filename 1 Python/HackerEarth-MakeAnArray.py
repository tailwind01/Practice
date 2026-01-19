#the description of this problem is super effed up
# I solved it using just intuition and trial and error
#
def solve (N, A):
    allSum = sum(A)
    maxElem = max(A)
    if allSum % (N-1) == 0 and maxElem <= allSum//(N - 1):
        return (allSum//(N-1))
    else:
        return -1
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out_ = solve(N, A)
    print (out_)
