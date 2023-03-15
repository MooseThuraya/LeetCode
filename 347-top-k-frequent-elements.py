class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        # [1,1,1,2,2,100] k=2

        # #build freq map
        # {
        #     1 (num): 3 (freq)
        #     3: 2 (freq)
        #     2: 2 (freq) 
        #     100: 1 (freq)
        # }

        # # key(freq) --> val([nums that have this freq....])
        # [[]0,[100]1,[ 2]2,[1]3,[]4,[]5,[]6] len(nums)

        freqMap = {}
        freqBucket = []
        res = []

        for i in range(len(nums)+1):
            freqBucket.append([])

        for num in nums:
            if freqMap.get(num) is None:
                # never seen this before
                freqMap[num] = 1
            else:
                # update freq
                freqMap[num] += 1
        
        for num, freq in freqMap.items():
            freqBucket[freq].append(num)
        
        # iterate in reverse to see which number w highest freq occurs first to append to res
        for i in range(len(freqBucket)-1, -1, -1):
            for bucketVal in freqBucket[i]:
                res.append(bucketVal)
                if len(res) == k:
                    return res
        # T(n) where n is the input list. last for loop runs in n+m. but n is greater than m (unique elements)
        # S(n) we can store n positions freqMap