class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:  # ← Check negative/zero first
            return False
        if n == 1:
            return True
        if n % 4 != 0:  # ← Then check divisibility
            return False
        return self.isPowerOfFour(n // 4)