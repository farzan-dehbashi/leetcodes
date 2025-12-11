class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '(' or char.isalnum():
                stack.append(char)
            elif char == ')':
                cur = []
                while stack[-1] != '(':
                    cur.append(stack.pop())
                stack.pop()
                stack = stack + cur
        return ''.join(stack)
