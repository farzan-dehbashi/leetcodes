class Solution:
    def isValid(self, s: str) -> bool:
        pars, stack = {')':'(', '}':'{', ']':'['}, []
        for char in s:
            if not char in pars:
                stack.append(char)
                continue
            elif not stack or not stack[-1] == pars[char]:
                return False
            else:
                stack.pop()
        return len(stack) == 0

