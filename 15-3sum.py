class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        hashSet = set()
        nums.sort()
        for k in range(len(nums)):
            i = 0
            j = len(nums)-1
            while i < j and i!=j and i!=k and j!=k:
                # we have a potential combo
                # check if i,j,k == 0
                if nums[i] + nums[j] + nums[k] == 0:
                    potentialCombo = [nums[i], nums[j], nums[k]]
                    potentialCombo.sort()
                    if tuple(potentialCombo) not in hashSet:
                        # first tiome seeing this
                        hashSet.add(tuple(potentialCombo))
                        res.append(potentialCombo)
                    i+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    # make number smaller
                    j-=1
                else:
                    #bigger
                    i+=1

        return res

        # T(n^2); nlogn + n^2 => n^. first loop goes n elements. second loop goes over n elements selectively. We only ever sort 3 elements if end up with a combo == 0
        # S(m), where m is the number of unique 3sum combinations