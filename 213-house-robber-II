class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        two=0
        one=0
        maxi1 = 0
        for i in range(len(nums)-1,0,-1):
            temp = max(two+nums[i], one)
            two = one
            one= temp
            if temp > maxi1:
                maxi1 = temp
        
        two=0
        one=0
        maxi2 = 0
        for i in range(len(nums)-2,-1,-1):
            temp = max(two+nums[i], one)
            two = one
            one= temp
            if temp > maxi2:
                maxi2 = temp
        
        return max(maxi1, maxi2)