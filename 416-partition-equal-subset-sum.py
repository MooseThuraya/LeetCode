class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Edge Case: where an sum of nums is odd.
        if sum(nums)%2==1:
            # If the sum is odd (11) we get 5.5. So, no result will be found.
            return False

        target = target//2
        dp = set([0])
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for num in dp:
                nextDP.add(nums[i] + num)
                nextDP.add(num)
            dp = nextDP
        return True if target in dp else False
        # T(n*sum(nums)) where n is len(nums)
        # S(sum(nums)) We are adding as many elements as our our target sum, sum(nums)