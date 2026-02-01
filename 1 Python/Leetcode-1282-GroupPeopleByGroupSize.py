#using defaultdict approach

from collections import defaultdict as dd
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gmap = dd(list)
        ans = []
        for p,s in enumerate(groupSizes):
            gmap[s].append(p)
            if len(gmap[s]) == s:
                ans.append(gmap[s])
                gmap[s] = []

        return ans

# first principles solution, not efficient..
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sieve = []
        for p,s in enumerate(groupSizes):
            psL = [s,p]
            sieve+=[psL]
        sieve.sort()
        ansArr = []
        indexCollection = []
        for i in range(len(sieve)):
            size,ind = sieve[i] 
            indexCollection.append(ind)
            if len(indexCollection)==size:
                ansArr.append(indexCollection)
                indexCollection = [] #resetting it 
        return ansArr
