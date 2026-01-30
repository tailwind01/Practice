class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [x for x in nums if x<pivot]+[pivot]*nums.count(pivot)+[z for z in nums if z>pivot]
