# solution to leetcode easy math
# minimum operations to make array divisible by k
# beats 99.76% submissions on leetcode, 0ms runtime
# based on modulo of sum of elements in the array

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums = list(map, int(), input().rstrip().split())
        # k = int(input())
        totK = sum(nums)
        return totK%k
    
        
