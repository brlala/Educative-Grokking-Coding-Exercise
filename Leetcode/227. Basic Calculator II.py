class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        val = 0
        op = '+'

        for i, x in enumerate(s):
            if x.isdigit():
                val = val * 10 + int(x)
            if x in '+-/*':
                if op == '+':
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)
                elif op == "*":
                    stack.append(stack.pop() * val)
                elif op == "/":
                    stack.append(int(stack.pop() / val))
                op, val = x, 0  # reset
        return sum(stack)

a = Solution()
a.calculate("3+2*2")