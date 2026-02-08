# same code with 2 different versions based on verbosity of the main case for which we have to solve
nc = int(input())

for _ in range(nc):
    n,s = map(int, input().rstrip().split())
    positions = list(map(int, input().rstrip().split()))
    begin = positions[0]
    end = positions[-1]
    # s can either be between beginning and end or outside of it
    if s<begin:
        moves = end-s
    elif s>end:
        moves = s-begin
    else:
        moves = min(abs(s-end),abs(s-begin))+end-begin
    print(moves)

# alternate version of higher verbosity
#
nc = int(input())

for _ in range(nc):
    n,s = map(int, input().rstrip().split())
    positions = list(map(int, input().rstrip().split()))
    begin = positions[0]
    end = positions[-1]
    # s can either be between beginning and end or outside of it
    if s<begin:
        moves = end-s
    elif s>end:
        moves = s-begin
    else:
        direction = "Forward" if (abs(s-end)<abs(s-begin)) else "Backward"
        if direction=="Forward":
            moves = abs(s-end) + end-begin
        else:
            moves = abs(s-begin)+end-begin
    print(moves)
