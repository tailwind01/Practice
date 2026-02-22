class Solution:
    def maximum69Number (self, num: int) -> int:
        stnum =''
        seen6 = 0
        for c in str(num):
            if seen6==0 and c=='6':
                seen6=1
                stnum+='9'
            else:
                stnum+=c

        return int(stnum)
