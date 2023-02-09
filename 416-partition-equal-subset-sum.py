class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Edge Case:
        if sum(nums)%2==1:
            # If the sum is odd (11) 5.5 wont be found
            return False

        dp = set()
        dp.add(0)

        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t)
                nextDp.add(t + nums[i])
            dp = nextDp
        
        return True if target in dp else False