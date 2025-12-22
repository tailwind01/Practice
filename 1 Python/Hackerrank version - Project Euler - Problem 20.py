#/a tailwind code.
import itertools as it
import operator as op
def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result

nc = int(input())

for _ in range(nc):
    n = int(input())
    nums = list(factorials_nums(n))
    numfact = str(nums[-1])
    sumd = 0
    for j in numfact:
        sumd+=int(j)
    print(sumd)

    
