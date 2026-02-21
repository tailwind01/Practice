import math as m
tc = int(input())

for _ in range(tc):
    l,r = map(int,input().rstrip().split())
    incl_diff = r-l+1
    # using the sum of arithmetic progression formula without looping
    # this simplifies to quadatric formula rearrangement
    ans = m.ceil((-1+m.sqrt(1+8*incl_diff))/2)
    print(ans)
