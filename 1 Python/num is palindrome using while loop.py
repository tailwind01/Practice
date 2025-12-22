def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        
        tr = 0
        l = len(numStr)
        ans = 0
        
        while(tr<l):
            if(numStr[tr]==numStr[l-1-tr]):
                ans = 1
                tr+=1
            else:
                ans = 0
                break
    
        return ans
