class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def helper(perm, excluded):
            if perm == [] or len(excluded) == len(nums):
                res.append(excluded)
                return
            for i in range(len(perm)):
                curPerm = []
                curExcluded = []
                curExcluded.append(perm[i])
                for j in range(len(perm)):
                    if i != j:
                        curPerm.append(perm[j])
                helper(curPerm, excluded + curExcluded)
            return
        helper(nums, [])
        return res
        # O(n!*n) --> T(n): we make (n)(n-1)(n-2)...n!.
        # S(n!) where we make n! in res. At the end for ex1, we have 6 when input nums is 3. 3*2*1 = 6

        # [[1,2,3][1,3,2], [2,1,3],[2,3,1], [3,1,2],[3,2,1]]
        #     [1,2,3]
        #     [2,3][1]
        #         [3][1,2]
        #             [][1,2,3]
        #         [2][1,3]
        #             [][1,3,2]
        #     [1,3][2]
        #         [3][2,1]
        #             [][2,1,3]
        #         [1][2,3]
        #             [][2,3,1]