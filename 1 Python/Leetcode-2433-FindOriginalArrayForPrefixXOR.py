class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]]+[pref[i]^pref[i-1] for i in range(1,len(pref))]

# another version
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i in range(1,len(pref)):
            elem = pref[i]
            ans.append(pref[i]^pref[i-1])
        return ans
