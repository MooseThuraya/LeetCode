class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build freq map
        # accumulate even sum
        # accumulate odd sum -1 for every odd number (to force even except one)
        # check if original string is odd, if it is, add one back
        
        hashMap = {}

        for l in s:
            if hashMap.get(l) is None:
                hashMap[l] = 1
            else:
                hashMap[l]+=1
        
        oddLen = 0
        evenLen = 0
        oddExists = False
        for k,v in hashMap.items():
            if v % 2 == 0:
                # its even
                evenLen+=v
            else:
                # its odd
                oddLen+=(v-1)
                oddExists = True
        
        if oddExists:
            # there exists an odd, so we add 1 more
            return evenLen+oddLen+1
        else:
            # we never had an odd number of freq in our map
            return evenLen+oddLen

        # Time: O(n)
        # Space: O(1); we store 26 characters at most so its O(1)