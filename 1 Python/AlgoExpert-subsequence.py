def isValidSubsequence(array, sequence):
    # Write your code here.
    ctr = 0
    for n in range(len(sequence)):
        if sequence[n] in array:
            ctr = 1
        else:
            ctr = 0
            break
    if ctr == 1:
        print ("Valid Subsequence")
    else:
        print ("Invalid Subsequence")
        
array = list(map(int,input().rstrip().split()))
subsequence = list(map(int,input().rstrip().split()))

print(isValidSubsequence(array,subsequence))
