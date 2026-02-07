import math as m
nc = int(input())

for _ in range(nc):
    n = int(input())
    order = list(map(int, input().rstrip().split()))
    L_ind1 = order.index(1)+1
    L_indN = order.index(n)+1
    R_ind1 = n-order.index(1)
    R_indN = n-order.index(n)
    opers = min(max(L_ind1,L_indN),max(R_ind1,R_indN),(L_ind1+R_indN), (R_ind1+L_indN))
    print(opers)
