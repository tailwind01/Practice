# Link - https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# O(1) time and space
# 0ms runtime, using basics of arithmetic progression

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m!=1: # for nontrivial cases
            allSum = n*(n+1)/2 #this is an arithmetic progression
            mMultiple = n//m #to find out the number of terms in another sub arithmetic progression
            mSum = mMultiple/2 * (m+m*mMultiple) #arithmetic progression of m's multiples
            nonMsum = allSum-mSum
            return int(nonMsum-mSum)
        else: #for trivial case, m=1
            return -int((n*(n+1)/2))
