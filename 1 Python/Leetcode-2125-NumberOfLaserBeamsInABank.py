# Both implementations are efficient at the job

# v2 = 0ms, beats 100% on runtime..
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        connections = 0
        prevDocket = 0
        for i in range(len(bank)):
            ctOf1s = bank[i].count('1')
            if ctOf1s!=0:
                connections += prevDocket*ctOf1s
                prevDocket = ctOf1s
        return connections

# v1 = 3ms runtime
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ct0s = []
        ct1s = []
        for i in range(len(bank)):
            ct0s.append(bank[i].count('0'))
            ct1s.append(bank[i].count('1'))
        
        connections=0
        ct1s_nonZero = [y for y in ct1s if y!=0]
        for x in range(1,len(ct1s_nonZero)):
            connections+=(ct1s_nonZero[x]*ct1s_nonZero[x-1])
            
        return connections
