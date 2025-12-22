# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. 
#If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

#Tailwind code.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        mn = 2*k
        rev = ''
        normcoll = ''
        for i in range(1,len(s)+1):
            if i%mn<=k and i%mn!=0:
                rev+=s[i-1]
            elif i%mn>k:
                normcoll+=s[i-1]
            else:
                normcoll+=s[i-1]
                ans+=rev[::-1]+normcoll
                rev=''
                normcoll=''
            
        return ans+rev[::-1]+normcoll

    
        
        
