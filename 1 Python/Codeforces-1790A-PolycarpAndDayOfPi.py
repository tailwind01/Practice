nc = int(input())

for _ in range(nc):
    strInp = str(input())
    rootCase = "314159265358979323846264338327" # obtained from testcase 1 :D

    #the constraints of the problem require us to get to 30 digits..
    ct = 0
    for i in range(len(strInp)):
        if strInp[i]==rootCase[i]:
            ct+=1
        else:
            break
            # no need to go any further, we get the f out. :D
    print(ct)
