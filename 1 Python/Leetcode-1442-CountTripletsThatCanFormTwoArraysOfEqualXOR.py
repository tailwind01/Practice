from collections import defaultdict as dd
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ct = 0
        cxor = 0
        cross = dd(lambda:[0,0])
        cross[0]=[1,0]
        for k in range(n):
            cxor^= arr[k]
            cidx = k+1
            if cxor in cross:
                occ,idsum = cross[cxor]
                ct+=(occ*k)-idsum
            cross[cxor][0]+=1
            cross[cxor][1]+=cidx
        return ct

# TLE Codes

from operator import xor
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j,len(arr)):
                    a = reduce(xor, arr[i:j])
                    b = reduce(xor, arr[j:k+1])
                    ans.append(a-b)
        return ans.count(0)

from operator import xor
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j,len(arr)):
                    a = reduce(xor, arr[i:j])
                    b = reduce(xor, arr[j:k+1])
                    if a==b:
                        ans+=1
        return ans

from operator import xor
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a = reduce(xor, arr[i:j])
                for k in range(j,len(arr)):
                    b = reduce(xor, arr[j:k+1])
                    if a==b:
                        ans+=1
        return ans
