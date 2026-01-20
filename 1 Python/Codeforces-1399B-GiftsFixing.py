#v2 pythonic shortcut

def giftfixingv2(s,A,B):
    minA = min(A)
    minB = min(B)
    moves = 0
    for x in range(s):
        moves += max(A[x]-minA,B[x]-minB)

    return moves
    
nc = int(input())

for _ in range(nc):
    size = int(input())
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))
    print (giftfixingv2(size,arr1,arr2))


#v1 - original logic
def giftfixing(s,A,B):
    minA = min(A)
    minB = min(B)
    aMoves = 0
    bMoves = 0
    commonMoves = 0
    for x in range(s):
        if A[x]!=minA:
            diffA = A[x]-minA
            aMoves+=diffA
        if B[x] != minB:
            diffB = B[x]-minB
            bMoves+=diffB
        if A[x]!=minA and B[x]!=minB:
            diffA = A[x]-minA
            diffB = B[x]-minB
            commonMoves+=min(diffA,diffB)
    
    return aMoves+bMoves-commonMoves
    
nc = int(input())

for _ in range(nc):
    size = int(input())
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))
    print (giftfixing(size,arr1,arr2))
