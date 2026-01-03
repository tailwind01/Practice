    nc = int(input())
     
    for _ in range(nc):
        n = int(input())
        s = list(map(str,input().rstrip().split()))
        res = []
        count = 1
        # first we shall separate consecutive elements and then find out their max length
        
        # collecting consecutive elements
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                res.append(s[i] * count)
                count = 1
        res.append(s[-1] * count)
        
        #looking for max length in resulting array
        maxLength = 0
        for r in res:
            if "0" in r and r.count("0")>maxLength:
                maxLength = r.count("0")
        print(maxLength)

