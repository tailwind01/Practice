class Solution:
    def mirrorDistance(self, n: int) -> int:
        comps = str(n)
        revNum = comps[::-1]
        return abs(int(revNum)-n)
          
