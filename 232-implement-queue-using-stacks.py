class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()