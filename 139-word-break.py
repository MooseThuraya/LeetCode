class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s)) and s[i: i + len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]
    
        # T(n*m) where n is len s and m is len of wordDict
        # S(n) where n is len s