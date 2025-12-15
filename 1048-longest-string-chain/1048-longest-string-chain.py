class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp, max_chain = {}, 1

        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                excluding_i = word[:i]+word[i+1:]
                if excluding_i in dp:
                    dp[word] = max(dp[word], dp[excluding_i] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain