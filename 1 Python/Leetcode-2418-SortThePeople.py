class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        valmap = list(zip(names, heights))
        heightMap = sorted(valmap,key = lambda x: x[1],reverse=True)
        ans = [i[0] for i in heightMap]
        return ans
