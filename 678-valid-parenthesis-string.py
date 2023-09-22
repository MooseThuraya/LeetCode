class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMax = 0
        leftMin = 0

        for c in s:
            if c == "(":
                leftMax, leftMin = leftMax + 1, leftMin + 1
            elif c == ")":
                leftMax, leftMin = leftMax - 1, leftMin - 1
            else:
                leftMax+=1
                leftMin-=1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

        # T(n)
        # S(1)