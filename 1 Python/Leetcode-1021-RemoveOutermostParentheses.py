class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openCt = 0
        closeCt = 0
        copied = list(s)        
        for i in range(len(copied)):
            c = copied[i]
            if c=="(":
                openCt+=1
            else:
                closeCt+=1

            if openCt==closeCt:
                copied[i-(openCt*2-1)]=""
                copied[i]=""
                openCt=0
                closeCt=0

        return "".join(copied)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openCt = 0
        closeCt = 0
        copied = list(s)
        for i,c in enumerate(s):
            if c=="(":
                openCt+=1
            else:
                closeCt+=1
            if openCt==closeCt:
                copied[i-(openCt*2-1)]=""
                copied[i]=""
                openCt=0
                closeCt=0
        return "".join(copied)
