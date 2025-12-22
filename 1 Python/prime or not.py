

    import math as m
    nc = int(input())
    ansAr = []
    for i in range(nc):
        verdict = 1 #by default we say the number is prime
        num = int(input())
        upperL = int(m.sqrt(num))+1
        if num > 1:
            for j in range(2,upperL):
                if num%j == 0: #divisible by any num
                    verdict = 0
                    break
            if verdict == 0: ansAr+=['no']
            else: ansAr+=['yes']
        
        else: ansAr+=['no']
     
    print("\n".join(ansAr))