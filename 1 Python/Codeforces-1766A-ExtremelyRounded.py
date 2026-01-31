import math as m

nc = int(input())

for _ in range(nc):
    n = int(input())
    ten_power = int(m.log10(n)//1)
    nearest_multiple = n//(pow(10,ten_power))
    if n<10: #trivial case
        print(n)
    else:
        print((ten_power*9)+nearest_multiple) #after identifying pattern this formula comes to be (hypothesized)
