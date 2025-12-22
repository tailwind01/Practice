````
#publisher: tailwind
#runtime: 62ms, memory: 0Kb, problem 732A-Buy a Shovel @codeforces
```````````
k,r = map(int,input().rstrip().split())

initMod = k%10

if initMod == r or initMod==0:
    print(1)
else:
    for i in range(1,10001): #as for given constraints max value is 10001 by hyp and anyway we are breaking the loop on finding solution
        calc = k*i
        if calc%10==r or calc%10==0:
            print(i)
            break
    
