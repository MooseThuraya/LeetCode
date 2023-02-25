class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one=1
        two=1
        for i in range(n-2,-1,-1):
            temp = one + two
            two = one
            one = temp
        return one
