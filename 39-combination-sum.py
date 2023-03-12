class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, combo, currentSum):

            # base cases
            if i >= len(candidates) or currentSum >= target:
                if currentSum == target:
                    res.append(combo)
                return
       
            # dont take and move on
            dfs(i + 1, combo, currentSum)

            # take and stay
            dfs(i, combo + [candidates[i]], currentSum + candidates[i])


        dfs(0, [], 0)

        return res

        # T/S(2^t) at a worst case, we the height of the decision tree will be t. Since 1 <= target <= 40