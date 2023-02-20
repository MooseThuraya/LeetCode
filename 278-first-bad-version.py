# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        m = (l+r)//2
        res = m
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m):
                res = m
                r = m-1
            elif not isBadVersion(m):
                l = m+1
            else:
                return res
        return res