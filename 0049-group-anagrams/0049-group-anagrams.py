class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        angs = collections.defaultdict(list)
        for word in words:
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord('a')] += 1
            angs[tuple(pattern)].append(word)
        return [word for word in angs.values()] 


      