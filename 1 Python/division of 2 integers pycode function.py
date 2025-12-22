def divide(self, dividend: int, divisor: int) -> int:
        intMin = -2**31
        intMax = 2**31 -1
        prohib = 0
        
        division = dividend/divisor
        
        if(divisor==0): 
            return "Not Defined"
        
        if(division>=0):
            ans = int(division//1)
        else:
            absDiv = abs(division)
            ans = -1 * int(absDiv//1)
        
        if(intMin<=ans and intMax>=ans):
            return ans
        elif (intMin>ans):
            return intMin
        elif (intMax<ans):
            return intMax
        else:
            return 0