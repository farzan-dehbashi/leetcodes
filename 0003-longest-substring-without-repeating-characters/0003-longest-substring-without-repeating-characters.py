class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, w, m = 0, set(), 0
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            m = max(m, len(w))
        return m