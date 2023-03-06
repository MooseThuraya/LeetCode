class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                res = op1 + op2
                stack.append(res)
            elif token == "-":
               op1 = stack.pop()
               op2 = stack.pop()
               res = op2 - op1
               stack.append(res)
            elif token == "*":
               op1 = stack.pop()
               op2 = stack.pop()
               res = op2 * op1
               stack.append(res)
            elif token == "/":
               op1 = stack.pop()
               op2 = stack.pop()
               res = op2 / op1
               stack.append(int(res))
            else:
                stack.append(int(token))
        return stack[0]
        # T(n)
        # S(n)