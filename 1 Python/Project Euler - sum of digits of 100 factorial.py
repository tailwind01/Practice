#/a tailwind code.
import itertools as it
import operator as op
def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result
nums = list(factorials_nums(100))
hundfact = str(nums[-1])
sumd = 0
for j in hundfact:
    sumd+=int(j)
print(sumd)
