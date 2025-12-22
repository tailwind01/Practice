#/tailwind code

n, k, l, c, d, p, nl, np = map(int, input().rstrip().split())

perml = (k*l)//nl
limes = (c*d)
salt = p//np

print(min(perml,limes,salt)//n)
