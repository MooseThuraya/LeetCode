class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if len(self.minStack) > 0 and val <= self.minStack[-1]:
            self.minStack.append(val)
        elif len(self.minStack) == 0:
            # is empty
            self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        poppedVal = self.stack.pop()
        if poppedVal == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()