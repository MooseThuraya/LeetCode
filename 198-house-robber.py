class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums.append(0)
        # nums.append(0)

        # two = nums[-1]
        # one = nums[-2]
        two = 0
        one = 0
        maximum = 0
        # for i in range(len(nums)-3, -1, -1):
        for i in range(len(nums)-1, -1, -1):
            temp = max(nums[i] + two, one)
            two = one
            one = temp
            if temp > maximum:
                maximum = temp
        return maximum

        #Re-simulate the backtracking recurrence relation
        #test case: [2,1,1,2] now works