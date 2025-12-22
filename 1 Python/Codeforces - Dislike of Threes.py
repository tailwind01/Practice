t = int(input())

numarr = []
for n in range(5000):
        if n%3==0:
            pass
        elif str(n)[-1]=='3':
            pass
        else:
            numarr+=[n]
    
for _ in range(t): 
    x = int(input())
    print(numarr[x-1])

