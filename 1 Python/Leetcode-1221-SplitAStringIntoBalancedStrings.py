class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lseen = 0
        rseen = 0
        ans = 0
        for c in s:
            if c=='L':
                lseen+=1
            else:
                rseen+=1
            if lseen==rseen:
                ans+=1
        return ans
