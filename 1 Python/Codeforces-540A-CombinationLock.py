n = int(input())
orig = str(input())
target = str(input())
moves = 0

for i in range(n):
    io = int(orig[i])
    it = int(target[i])
    moves+=min(abs(io-it),10-abs(it-io))

print(moves)
