class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        maxP,minP = 1, 1

        for n in nums:
            tmp = maxP * n
            maxP = max(tmp, minP * n, n)
            minP = min(tmp, minP * n, n)
            res = max(res, maxP)

        return res