class Solution:
    def maxDistinct(self, s: str) -> int:
        uniqueStarts = []

        for l in s:
            if l not in uniqueStarts:
                uniqueStarts.append(l)

        return len(uniqueStarts)
