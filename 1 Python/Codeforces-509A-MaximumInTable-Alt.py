import math as m
n = int(input())
numerator = range(n,n+(n-1),1)
denominator = range(1,1+len(numerator),1)
print(int(m.prod(numerator)/m.prod(denominator)))
