# 0ms solution using list compreshension, beats 100% in memory and runtime

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([x%2 for x in nums])
