lower = 900
upper = 999
numTuples = []
maxPal = 0
for i in range(lower, upper+1):
    for j in range(lower, upper+1):
        calc = i*j
        if str(calc)==str(calc)[::-1]:
            if maxPal<calc:
                maxPal = calc
                
print(maxPal)

            
        
