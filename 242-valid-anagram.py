class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for l in s:
            if hashMap.get(l) is None:
                hashMap[l] = 1
            else:
                hashMap[l] += 1
        
        for l in t:
            if hashMap.get(l) is None:
                return False
            else:
                hashMap[l]-=1
        for k,v in hashMap.items():
            if v != 0:
                return False

        return True