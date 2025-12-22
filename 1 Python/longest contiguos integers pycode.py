def checkZeroOnes(self, s: str) -> bool:
        #creation of lengthArrays
        
        neS1 = s.replace("0"," ")
        stringasList1 = list(neS1.split())
        lenArr1=[]

        for i in range(len(stringasList1)):
            lenArr1+=[len(stringasList1[i])]
        
        neS0 = s.replace("1"," ")
        stringasList0 = list(neS0.split())
        lenArr0=[]

        for i in range(len(stringasList0)):
            lenArr0+=[len(stringasList0[i])]
        
        #compiling counts
        c1 = s.count('1')
        c0 = s.count('0')
        
        if c1>0 and c0>0:
            return max(lenArr1)>max(lenArr0)
        elif c1==0 and c0>0:
            return 0
        elif c1>0 and c0==0:
            return 1
        else:
            return 0