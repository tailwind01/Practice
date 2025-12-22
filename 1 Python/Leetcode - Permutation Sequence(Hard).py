#create the ultimate list outside the function and then call values from that list
#############################################################################
###############################STACK1########################################
from itertools import permutations as p
digits = ["1","2","3","4","5","6","7","8","9"]
motherList = []  
for num in range(1,10):
    daughterList = []
    allPerms = list(set(p(digits[:num],num)))
    for perm in allPerms:
            givenNum = int(''.join(perm))
            daughterList+=[givenNum]
    daughterList.sort()
    motherList+=[daughterList]    

#############################################################################
#####################SOLUTION CALL__#########################################
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return str(motherList[n-1][k-1]) #as Python works 0-indexed
