from collections import Counter as ctr
nc = int(input())

for _ in range(nc):
    size = int(input())
    arr = list(map(int, input().rstrip().split()))
    ctList = ctr(arr)
    distincts = list(ctList.values())
    flag = 0
    
    if len(distincts )==1: flag=1
    elif len(distincts)==2: 
        if(abs(distincts[0]-distincts[1])<=1): 
            flag = 1
    
    print("Yes" if flag==1 else "No")

##Incorrect submission follows for reference (commented out here on) - spent nearly 2 hours :<(
#
# import math as m
# nc = int(input())
#
# for _ in range(nc):
#     size = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     inSort = sorted(arr)
#     if size>3:
#         flag = 1
#         midPt = (size+1)//2
#         Half1 = []
#         Half2 = []
#         for i in range(midPt):
#             Half1.append(inSort[i])
#         for k in range(midPt,size):
#             Half2.append(inSort[k])
#         Half2_Rev = Half2[::-1]
#
#         Pairs = list(zip(Half1, Half2_Rev)) #pairing so that sum is balanced across the board.
#         flag = 1 #let's assume by default that the sums are equal all across the board
#         kSum = sum(Pairs[0]) #sum of the first tuple we encounter that would ideally have balanced sum
#         for p in range(1,len(Pairs)):
#             #conditions for the flag to hold: sum has to be equal, (p-1)[1]& (p)[0] sum has to be kSum
#             if Pairs[p][1]+Pairs[p-1][0]!=kSum or kSum!=sum(Pairs[p]):
#                 flag = 0
#                 break #if we encounter a situation like this, flag is set to zero and we move out
#         print("Yes" if flag==1 else "No")
#     else:
#         if size==2:
#             print("Yes")
#         else:
#             print("Yes" if inSort[1]==inSort[0] or inSort[1]==inSort[2] else "No")
