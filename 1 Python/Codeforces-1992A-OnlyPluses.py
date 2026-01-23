# 2 versions of the code
# v1 is a brute force approach
# v2 is more elegant and refined
# while both the codes solve the problem, v2 is aimed at being parsimonious - albeit requires sorting 5 times

#v2 O(1)
import math as m
nc = int(input())
for _ in range(nc):
    inp = sorted(list(map(int,input().rstrip().split()))) #sorting at input stage only..
    sieve = inp
    totMoves = 5
    
    for x in range(totMoves):
        sieve.sort() #we sort at every iteration of the loop to gain biggest amt
        sieve[0]+=1
    
    print(m.prod(sieve))

#v1 brute force - does not show on runtime, but this is inefficient. documenting it as a f-up committed overengineering..
import math as m
nc = int(input())
for _ in range(nc):
    inp = sorted(list(map(int,input().rstrip().split()))) #sorting at input stage only..
    totMoves = 5 #the problem is allocation of these 5 greedily
    #we do possible allocations at the outset for determination as we have already sorted input
    allocations = [[5,0,0],[4,1,0],[3,2,0],[3,1,1],[2,2,1]]
    prodsArr = []
    
    for a in range(len(allocations)):
        currAll = allocations[a]
        newArr = [x+y for x,y in zip(currAll,inp)]
        prodsArr.append(m.prod(newArr))
    
    print(max(prodsArr))
