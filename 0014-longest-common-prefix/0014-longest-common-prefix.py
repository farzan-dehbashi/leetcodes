class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_str, max_str = min(strs), max(strs)
        
        for i in range(min(len(min_str), len(max_str))):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str