from itertools import combinations as comb
from operator import or_
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxBor = reduce(or_,nums)
        ctr = 0
        for i in range(1,len(nums)+1,1):
            for ss in comb(nums,i):
                ssOr = reduce(or_,ss)
                if ssOr==maxBor:
                    ctr+=1
        return ctr
