class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Find lexicographically smallest and largest
        min_str = min(strs)
        max_str = max(strs)
        
        # Compare only these two strings
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        
        return min_str