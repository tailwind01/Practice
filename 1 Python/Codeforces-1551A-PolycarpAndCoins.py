nc = int(input())

for _ in range(nc):
    n = int(input())
    intDiv = n//3
    
    if n%3==0:
        print(str(intDiv)+" "+str(intDiv))
    elif n%3==1:
        print(str(intDiv+1)+" "+str(intDiv))
    else:
        print(str(intDiv)+" "+str(intDiv+1))
