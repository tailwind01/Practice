import itertools as it
import operator as op

#save the result locally for maximum number that can occur
result = list(it.accumulate(it.chain([1], range(1, 1+10000)), op.mul))

class Solution: 
    def trailingZeroes(self, n: int) -> int:
        mystr = str(result[n])[::-1]
        ct = 0
        i = 0
        while(mystr[i]=='0'):
            ct+=1
            i+=1
        
        return ct
