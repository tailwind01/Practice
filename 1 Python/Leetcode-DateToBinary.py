class Solution:
    def convertDateToBinary(self, date: str) -> str:
        yyyy = date[:4]
        mm = date[5:7]
        dd = date[8:]
        outputStr = bin(int(yyyy))[2:]+"-"+bin(int(mm))[2:]+"-"+bin(int(dd))[2:]
        return outputStr
