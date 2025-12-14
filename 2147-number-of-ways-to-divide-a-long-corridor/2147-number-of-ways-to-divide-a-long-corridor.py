class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        seats = [i for i, char in enumerate(corridor) if char == 'S']
        if len(seats)%2 != 0 or len(seats) < 2:
            return 0
        
        ways = 1
        for i in range(2, len(seats), 2):
            gap = seats[i] - seats[i-1]
            ways = (ways*gap) % MOD
        return ways