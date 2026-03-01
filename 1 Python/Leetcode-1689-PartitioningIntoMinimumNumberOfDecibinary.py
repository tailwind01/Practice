class Solution:
    def minPartitions(self, n: str) -> int:
        ph = "987654321"
        ans = 0
        for c in ph:
            if c in n:
                ans = int(c)
                break
        return ans
