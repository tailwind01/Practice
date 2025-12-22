# Leetcode problem - https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# List traversal output
# O(n) time and space

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l1 = []
        l2 = []
        for x in range(n+1):
            if x%m!=0:
                l1.append(x)
            else:
                l2.append(x)
        return sum(l1)-sum(l2)
