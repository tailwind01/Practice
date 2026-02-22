# 2 versions, one with dictionary (O(n)), other with normal list index search(O(n^2))
#
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        es = {char:i for i,char in enumerate(s)}
        ans = 0
        for j,c2 in enumerate(t):
            ans+=abs(es[c2]-j)
        return ans

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(t.index(c)-s.index(c)) for c in s)
