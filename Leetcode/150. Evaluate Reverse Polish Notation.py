# Postfix Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]):
        if not tokens: return
        stack = []
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            if t in '+-*/':
                r = stack.pop()
                l = stack.pop()
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                elif t == '/':
                    stack.append(int(float(l) / r))
        return stack[0]
