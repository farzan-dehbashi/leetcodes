class Solution:
    def countPairs(self, ds: List[int]) -> int:
        freqs, count, pows = {}, 0, {2**x for x in range(22)}
        for m in ds:
            for power in pows:
                complement = power - m
                count = (freqs.get(complement, 0) + count) % (10 ** 9 + 7)
            freqs[m] = freqs.get(m, 0) + 1
        return count