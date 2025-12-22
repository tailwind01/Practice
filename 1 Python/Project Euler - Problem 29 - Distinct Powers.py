#/ a tailwind code
anslist  = []

for i in range(2,101):
    for j in range(2,101):
        elem = str(pow(i,j)) #convert to string to keep
        if elem not in anslist:
            anslist+=[elem]
print(len(anslist))
