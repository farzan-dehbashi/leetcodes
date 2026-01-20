class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp, ml = collections.defaultdict(int), 1

        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                excluding_i = word[:i] + word[i+1:]
                if excluding_i in dp:
                    dp[word] = max(dp[word], dp[excluding_i] + 1)
            ml = max(ml, dp[word])
        return ml