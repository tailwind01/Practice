# Problem Link-https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opers = 0 
        for n in nums:
            if n%3!=0:
                opers+=1
        return opers

        
