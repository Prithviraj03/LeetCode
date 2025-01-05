class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openclose = {')' : '(',']' : '[','}' : '{'}

        for x in s:
            if x in openclose:
                if stack and stack[-1] == openclose[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False