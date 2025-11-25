class Solution:
    def isValid(self, s: str) -> bool:
        pars, stack = {')':'(', '}':'{', ']':'['}, []
        for char in s:
            if not char in pars:
                stack.append(char)
            else:
                if not stack or not stack[-1] == pars[char]:
                    return False
                stack.pop()
        return len(stack) == 0


