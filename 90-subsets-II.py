class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def helper(i , subset):
            # base case
            if i >= len(nums):
                res.append(subset)
                return
            
            # 1st call: taking element
            helper(i + 1, subset + [nums[i]])

            # check for duplicates (we know nums is sorted)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            # 2nd call: not take element
            helper(i + 1, subset)

        helper(0, [])

        return res

        # T(k*2^n) where n is the len(nums), and k is the average len(subset) (worst case n), it takes k time to append subset to res
        # S(k*2^n): we are generating 2^n subsets in our decision tree. at the end we are storing k subsets in our res.
        # OR (n*2^n)

        # Code snippet helps with concept:
        # list = [1,2,3,4,5,6,7,8,9,10]
        # for i in range(len(list)): n time to loop
        #     temp = [i]*i          n to create
        #     list.append(temp)     n to append list (worst)

        # O(n*(n+n)) --> O(n^2) 