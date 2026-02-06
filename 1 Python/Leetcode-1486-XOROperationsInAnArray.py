from operator import xor
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        tempArr = []
        for i in range(n):
            tempArr.append(start+2*i)
        return reduce(xor, tempArr)
