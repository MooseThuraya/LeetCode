class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenMap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in "({[":
                stack.append(c)
            if c in ")]}" and not stack:
                # close and empty stack
                return False
            if c in ")]}"and parenMap[c] != stack[-1]:
                # check if close does not have matching open
                return False
            elif c in ")]}" and parenMap[c] == stack[-1]:
                # check if close does have matching open
                stack.pop()

        # if we still have elements in the end, we havent closed all the brackets
        return False if stack else True
        #Runs in n time
        #Runs in n space