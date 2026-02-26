class Solution:
    def numSteps(self, s: str) -> int:
        asL = list(s)
        steps = 0
        while(len(asL)>1):
            if asL[-1]=='0':
                asL.pop()
                steps+=1
            else:
                steps+=1
                while asL and asL[-1]=='1':
                    asL.pop()
                    steps+=1
                if not asL:
                    asL=["1"]
                else:
                    asL[-1]='1'
        return steps
