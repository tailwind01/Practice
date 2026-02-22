class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ct1s = s.count('1')
        ct0s = s.count('0')
        ans = '1'*(ct1s-1)+'0'*ct0s+'1'
        return ans
