class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stock = prices[0]
        maxProf = 0
        
        for p in prices:
            if p < stock:
                stock = p
            profit = p - stock
            maxProf = max(maxProf, profit)
        return maxProf