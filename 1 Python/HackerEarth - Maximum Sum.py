#/ tailwind code, works well
import bisect as b
n = int(input())
l = list(map(int, input().rstrip().split()))
#bisection at zero, and we want maximum no of elements so even trivial zeros need to be included in the count
l.sort()
z_ind = b.bisect(l,0)
b.insort_left(l,0)

if z_ind == len(l)-1:
    ansAr = [str(l[-2]),str(1)]
else:
    ansAr = [str(sum(l[z_ind+1:])), str(len(l[z_ind+1:])+l.count(0)-1)] #we deduct 1 as for bisection we had added an extra element
print(" ". join(ansAr))
