def reverse(self, x: int) -> int:
        intAsStr = str(x)
        arr = list(intAsStr)
        ansArr = []
        if(arr[0]=="-"):
            ansArr+=["-"]
            ansArr+=arr[::-1]
            final = ansArr[:-1]
        else:
            ansArr+=arr[::-1]
            final = ansArr
        ans = int("".join(final))
        
        if(ans<(2**31 - 1) and ans>((-2)**31)):
            return ans
        else:
            return int(0)