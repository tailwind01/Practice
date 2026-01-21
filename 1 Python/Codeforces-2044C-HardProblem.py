def hardProblem(m,a,b,c):
    # we wil have to function row-wise, the bottlneck is assignment of c's
    totSeats = 2*m
    row1 = min(m,a)
    row2 = min(m,b)
    row1Rem = m-row1
    row2Rem = m-row2
    totRem = row1Rem+row2Rem
    
    return row1+row2+min(totRem,c)
    
nc = int(input())

for _ in range(nc):
    m,a,b,c = map(int, input().rstrip().split())
    print(hardProblem(m,a,b,c))
