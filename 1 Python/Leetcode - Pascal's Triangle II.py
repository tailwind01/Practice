#/tailwind code
from math import comb as c

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        subl = []
        numelems = rowIndex
        for i in range(numelems+1):
            subl+=[c(numelems,i)]
        return subl
