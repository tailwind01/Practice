class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ansArr = nums + nums[::-1]
        return ansArr
