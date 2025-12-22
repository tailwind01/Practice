#/tailwind
import math as m
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x!=0:
            powOf_exp = m.log(x)
            sqrootusingE = powOf_exp/2

            ansNum = m.exp(sqrootusingE)
        
        else:
            ansNum=0
            
        if m.ceil(ansNum)-ansNum<0.0000000001:
            return m.ceil(ansNum)
        else:
            return m.floor(ansNum)
