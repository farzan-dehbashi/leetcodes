class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need, required, formed, window, l, min_len, start = collections.Counter(t), len(collections.Counter(t)), 0, collections.defaultdict(int), 0, float('inf'), 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                
                char = s[l]
                window[char] -= 1
                if char in need and window[char] < need[char]:
                    formed -= 1
                
                l += 1
        
        return "" if min_len == float('inf') else s[start:start + min_len]