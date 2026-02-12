from itertools import combinations as cmb
from operator import xor
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorTot = 0
        for i in range(1,len(nums)+1,1):
            cc = cmb(nums,i)
            for c in cc:
                xorTot+=reduce(xor,c)
        return xorTot
