class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ph = [(n,format(n,'032b').count('1')) for n in arr]
        ans = [x[0] for x in sorted(ph, key= lambda x:(x[1],x[0]))]
        return ans
