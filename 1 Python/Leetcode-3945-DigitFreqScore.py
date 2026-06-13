class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        nls = list(str(n))
        ans = 0
        for i in nls:
            ans+=int(i)
        return ans
