class Solution:
    def binaryGap(self, n: int) -> int:
        binrep = format(n,'032b')
        # we need to keep track of only the last 1
        lastseen1 = binrep.index('1')
        maxDiff = 0
        for i in range(lastseen1+1,len(binrep)):
            curr = binrep[i]
            if curr=='1':
                diff =  i-lastseen1
                lastseen1 = i
                if diff > maxDiff:
                    maxDiff = diff
        return maxDiff
