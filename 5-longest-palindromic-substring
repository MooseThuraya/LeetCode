class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def checkPali(l, r):
            # DONT FORGET THE EQUAL SIGN --> '='
            while l >= 0 and r < len(s) and s[l]==s[r]:
                curPalLen = r-l+1
                if curPalLen > self.maxi:
                    self.maxi = curPalLen
                    self.maxPal = s[l:r+1]
                r+=1
                l-=1
            return
        
        self.maxi = 1
        self.maxPal = s[0]
        for i in range(0,len(s)):
            # Even Case
            r = i+1
            checkPali(i,r)

            # Odd Case
            l = i-1
            checkPali(l,r)

        return self.maxPal