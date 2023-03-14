class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def helper(i , subset):
            # base case
            if i >= len(nums):
                res.append(subset)
                return
            
            # 1st call: taking element
            helper(i + 1, subset + [nums[i]])

            # 2nd call: not take element
            helper(i + 1, subset)

        helper(0, [])

        return res