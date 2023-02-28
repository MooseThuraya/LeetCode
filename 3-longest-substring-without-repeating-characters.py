class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in hashSet and l < len(s):
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            maxLen = max(maxLen, len(hashSet))
        return maxLen

        #T(n)
        #S(n)