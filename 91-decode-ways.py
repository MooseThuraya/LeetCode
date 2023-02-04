class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Two Variable -  Dynamic Programing Solution
        # T(n)
        # S(1)

        two = 1
        one = 1
        temp = 0

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                temp = 0
                two = one
                one = temp
                continue
            
            temp += one

            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                temp+=two
            two = one
            one = temp
            temp = 0 # You have to reset temp, otherwise u accumulate which WRONG!

        return one

        return helper(0)

        #--------------------------------------------------------------
        
        # Dynamic Programing Solution
        # T(n)
        # S(n)

        dp = [0] * (len(s) + 1)

        dp[-1] = 1

        for i in range(len(s)-1, -1,-1):

            if s[i] == "0":
                dp[i] = 0
                continue
            
            dp[i] += dp[i+1]

            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i]+=dp[i+2]

        return dp[0]      

        #--------------------------------------------------------------
                      

        # Memoization Solution
        # T(n)
        # S(n)

        dp = {len(s): 1}

        def helper(i):
            if i in dp:
                return dp[i]
            
            # Checking a singular number
            if s[i] == "0":
                return 0
            
            res = helper(i + 1)
            
            # Check a pair
            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res+= helper(i + 2)

            dp[i] = res
            
            return res