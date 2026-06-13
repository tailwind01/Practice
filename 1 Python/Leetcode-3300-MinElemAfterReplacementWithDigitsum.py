# storing only the minsum every iteration
#
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minsum = 36
        for n in nums:
            nls = list(str(n))
            ts = 0
            for d in nls:
                ts+=int(d)
            if ts<minsum:
                minsum = ts
        return minsum


## Crude version
class Solution:
    def minElement(self, nums: List[int]) -> int:
        sdarr = []
        for n in nums:
            ns = list(str(n))
            ts = 0
            for x in ns:
                ts+=int(x)
            sdarr+=[ts]
        return min(sdarr)
