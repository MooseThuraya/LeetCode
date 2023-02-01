class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def checkPali(l,r):
            while l >= 0 and r < len(s) and s[l]==s[r]:
                self.count+=1
                r+=1
                l-=1
            return

        self.count = 0
        for i in range(len(s)):
            self.count+=1

            # Even Case
            r = i+1
            checkPali(i, r)

            # Odd Case
            l = i-1
            checkPali(l,r)
        
        return self.count