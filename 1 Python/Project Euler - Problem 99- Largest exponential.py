# ##Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

# a tailwind implementation
import math as m
l = 1000
mod = pow(10,9)+7
inpl=[]
for i in range(l):
    base, exponent = map(int, input().split(","))
    #we will calculate values using logarithmic rules
    ln_ans = exponent*m.log(base)
    inpl+=[ln_ans]

maxnum = max(inpl) #naturally, number with largest ln_ans is largest

print(inpl.index(maxnum)+1)
    
