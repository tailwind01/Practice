from collections import Counter as ctr
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kfreq = sorted(list(ctr(nums).items()), key=lambda x: x[1], reverse = True)[:k]
        return [k[0] for k in kfreq]
