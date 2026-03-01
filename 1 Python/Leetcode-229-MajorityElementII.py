from collections import Counter as ctr
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ts = len(nums)/3
        asCtr = ctr(nums)
        ans = []
        for item,count in asCtr.items():
            if count>ts:
                ans.append(item)
        return ans

# Boyer Moore
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        cand1, cand2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        for cand in [cand1, cand2]:
            if nums.count(cand) > len(nums) // 3:
                result.append(cand)
 
        return list(set(result))
