class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cumsum = 0
        for x in operations:
            if x[1]=="-":
                cumsum-=1
            else:
                cumsum+=1

        return cumsum
        
