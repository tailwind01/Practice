# 1ms
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort(), students.sort()
        return sum(abs(x-y) for x,y in zip(seats,students))

# 3ms
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        return sum(abs(seats[x]-students[x]) for x in range(n))

#1ms
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        moves = 0
        for x in range(n):
            moves+=abs(seats[x]-students[x])
        return moves
