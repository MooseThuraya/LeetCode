class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l=0
        r=len(nums)-1
        i=0
        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
                i+=1
            else:
                i+=1
            
        return nums

        # Edge case: dont increment i if swap 2

        # T(n): where n in len of nums
        # S(1): no extra space used