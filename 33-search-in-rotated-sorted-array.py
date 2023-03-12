class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:  # we know this side is sorted (good side)
                if nums[m] >= target and nums[l] <= target: # Equal is important for it to be included in this side!!!
                    #its on this good side
                    r = m-1
                else:
                    # it has to be on the other side (bad side)
                    l = m+1
            else:        
                # bad side
                if nums[r] >= target and nums[m] <= target: # Equal is important for it to be included in this side!!!
                    # target falls on this side
                    l = m+1
                else:
                    # target falls on other side
                    r = m-1
        return -1

        # T(logn)
        # S(1)