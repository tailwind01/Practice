# defining a function for the division

def fd(arr):
    c1 = arr.count(1)
    w1 = c1
    c2 = arr.count(2)
    w2 = 2*c2
    
    # stipulation1: each modulo candy of 2 grams has to be offset by 2 candies of 1 gram
    s1 = 2*(c2%2)
    
    # stipulation2: after having enough to offset 2 grams, the 1 gram candies left should be even
    s2 = c1-s1
    
    #stipulation3: s2 has to be a positive number to make sense
    if s2>=0 and s2%2==0:
        return "YES"
    else:
        return "NO"

nc = int(input())

for _ in range(nc):
    n = int(input())
    candies = list(map(int, input().rstrip().split()))
    print(fd(candies))
