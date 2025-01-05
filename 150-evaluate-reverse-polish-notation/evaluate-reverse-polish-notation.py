class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                add = int(stack[-2]) + int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)                
                stack.append(add)
            elif i == '-':
                sub = int(stack[-2]) - int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(sub)
            elif i == '*':
                mul = int(stack[-2]) * int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)                
                stack.append(mul)
            elif i == '/':
                div = int(int(stack[-2]) / int(stack[-1]))
                stack.pop(-1)
                stack.pop(-1)                
                stack.append(div)
            else:
                stack.append(i)

        return int(stack[-1])