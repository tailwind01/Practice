#https://www.hackerrank.com/challenges/quicksort1/problem

def quickSort(arr):
    p = arr[0] #pivot equalisation
    e = [str(p)]
    l=[]
    r=[]
    for i in arr[1:]:
        if i<p:
            l+=[str(i)]
        elif i>p:
            r+=[str(i)]
        else:
            e+=[str(i)]
    comAr = l+e+r
    return " ".join(comAr)

n = int(input())
a = list(map(int, input().rstrip().split()))
print(quickSort(a))

####
#STDIN
#50
#-13 68 -43 -71 -39 -10 40 -49 -19 -3 -70 -62 -76 -94 -73 64 72 -5 88 2 -63 92 -40 16 49 47 -86 -51 -9 -14 96 74 -22 -34 38 -12 6 63 19 -69 14 -90 -27 76 54 57 -87 -91 43 -92
###
#STDOUT
#-43 -71 -39 -49 -19 -70 -62 -76 -94 -73 -63 -40 -86 -51 -14 -22 -34 -69 -90 -27 -87 -91 -92 -13 68 -10 40 -3 64 72 -5 88 2 92 16 49 47 -9 96 74 38 -12 6 63 19 14 76 54 57 43