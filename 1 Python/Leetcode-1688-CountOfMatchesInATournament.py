# 2 versions of the solution, one explains the steps, other is mathematical
# I prefer the mathematical reduction
# though for some effed up reason the O(1) solution shows 52ms runtime on Leetcode and algorithmic one shows 39ms

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n>=2:
            if n % 2 == 0:
                n=n//2
                matches+=n
            else:
                matches+=((n-1)//2)
                n=(n+1)//2 
        return matches

