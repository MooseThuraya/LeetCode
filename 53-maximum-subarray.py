class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        # Set maxSum to smallest number so it passes test case [-1]
        maxSum = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0
        return maxSum