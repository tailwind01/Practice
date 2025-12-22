#/tailwind code
class Solution:
    def romanToInt(self, s: str) -> int:
        
        symarr=["I","V","X","L","C","D","M"]
        valarr=[1,5,10,50,100,500,1000]
        num = 0
        l = len(s)
        
        for c in range(len(s)):
            if s[c]=="I" and s[min(l-1,c+1)] in ["V","X"]:
                if s[c+1]=="V":
                    num+=4
                    num-=5
                else:
                    num+=9
                    num-=10
            elif s[c]=="X" and s[min(l-1,c+1)] in ["L","C"]:
                if s[c+1]=="L":
                    num+=40
                    num-=50
                else:
                    num+=90
                    num-=100
                    
            elif s[c]=="C" and s[min(l-1,c+1)] in ["D","M"]:
                if s[c+1]=="V":
                    num+=400
                    num-=500
                else:
                    num+=900
                    num-=1000
            else:
                valInd = symarr.index(s[c])
                num+=valarr[valInd]
        
        return num
            
        
        
