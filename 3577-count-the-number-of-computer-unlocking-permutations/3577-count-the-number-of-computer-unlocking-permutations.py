class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity[1:]) <= complexity[0]:
            return 0

        def factorial(n):
            if n in [0,1]:
                return n
            return n * factorial(n-1) % (10**9 + 7)
        
        return factorial(len(complexity)-1)