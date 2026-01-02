import math as m
def solve (N):
    ph = int(m.log2(N))
    return pow(2,ph)

T = int(input())
for _ in range(T):
    N = int(input())
    out_ = solve(N)
    print (out_)
