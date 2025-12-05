class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        need, need_len, found_len, w, l, min_len, start = collections.Counter(t), len(collections.Counter(t)), 0, collections.defaultdict(int), 0, float('inf'), float('inf')

        for r in range(len(s)):
            w[s[r]] += 1

            if s[r] in need and need[s[r]] == w[s[r]]:
                found_len += 1
            
            while l<=r and found_len == need_len:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    start = l
                
                w[s[l]] -= 1
                if s[l] in need and need[s[l]] > w[s[l]]:
                    found_len -= 1
                l += 1
        return '' if min_len == inf else s[start:start+min_len]