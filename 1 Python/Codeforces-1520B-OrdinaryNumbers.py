#mathematical approach to solve the problem.

import math as m
nc = int(input())

for _ in range(nc):
    x = int(input())
    ml10_int = int(m.log10(x))
    baseline = ml10_int * 9
    numDigits = ml10_int + 1
    relNum = int("1"*numDigits) #baseline number for comparison afterwards
    ans = baseline + (x//relNum)
    print(int(ans))
