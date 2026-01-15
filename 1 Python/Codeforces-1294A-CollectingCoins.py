nc=int(input())

for _ in range(nc):
    a,b,c,n = map(int, input().rstrip().split())
    sieveSum = a+b+c+n
    maxVal = max(a,b,c)
    diffsToCover = [abs(maxVal-a),abs(maxVal-b),abs(maxVal-c)] #each value is compared with the max of 3
    totDiff = sum(diffsToCover)
    
    print("Yes" if sieveSum%3==0 and totDiff<=n  else "No")
