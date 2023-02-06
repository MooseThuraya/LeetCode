class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1)
        # Set zero-th amount = 0
        dp[0] = 0

        # Go over every other amount from 1, amount 
        for a in range(1, amount+1): # (amount non-inclusive)
        # Test every coin to see which coin will provide sol.
        # Ex. a=5, c=5 --> a-c or 5-5 = 0, chosen to be stored in dp[a]
            for c in coins:
                if a - c >= 0:
                    # for our current amount, we want to see if amount - curCoin is the sol
                    dp[a] = min(dp[a], 1 + dp[a-c])
        # if there has been no change to the last element in our DP (happens to be dp[amount+1]), return -1, otherwise, we got it.
        if dp[-1] == amount+1:
            return -1
        else:
            return dp[-1]