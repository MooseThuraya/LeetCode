class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magFreq = {}
        for let in magazine:
            if magFreq.get(let) is None:
                magFreq[let] = 1
            else:
                magFreq[let]+=1
        
        for let in ransomNote:
            if magFreq.get(let) is None:
                return False
            else:
                magFreq[let] -=1
                if magFreq[let] < 0:
                    return False
        return True

        # Time (m) where m is time to iterate over magazine, even if ransomNote is longer, we break when False
        # Space (1) arguably, we only store 26 letters at worst case, which is constant