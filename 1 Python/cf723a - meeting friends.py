#a tailwind publication, runtime 62ms, memory 0Kb, carpe fucking diem//
l = list(map(int, input().rstrip().split()))
mp = (min(l)+max(l))//2
ans = (max(l)-mp)+(mp-min(l))
print(ans)
