class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ansL = [first]*(len(encoded)+1)
        for i in range(len(encoded)):
            ansL[i+1]=ansL[i]^encoded[i]
        return ansL

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ansL = [first]*(len(encoded)+1)
        for i,n in enumerate(encoded):
            ansL[i+1]=ansL[i]^n
        return ansL

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ansL = [first]
        for n in encoded:
            ansL.append(ansL[-1]^n)
        return ansL

from itertools import accumulate
from operator import xor
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return list(accumulate(encoded,xor,initial=first))

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lastXor = first
        ans = [first]
        for i in encoded:
            lastXor = i ^ lastXor
            ans.append(lastXor)
        return ans
