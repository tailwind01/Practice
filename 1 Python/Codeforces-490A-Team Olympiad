n = int(input())
st_skill = list(map(int,input().split()))
math_ct=0
math_ind=[]
prog_ct=0
prog_ind=[]
pe_ct=0
pe_ind=[]
teams=[]
for s in range(n):
    if st_skill[s]==2:
        math_ct+=1
        math_ind+=[s+1]
    elif st_skill[s]==1:
        prog_ct+=1
        prog_ind+=[s+1]
    else:
        pe_ct+=1
        pe_ind+=[s+1]

w=min(math_ct, prog_ct, pe_ct)
if w>=1:
    print(w)
    for l in range(w):
        print(prog_ind[l],math_ind[l],pe_ind[l])
else:
    print(w)
    
