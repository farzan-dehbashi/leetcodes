class Solution:
    def isValid(self, s: str) -> bool:
        pars, stack = {')':'(', '}':'{', ']':'['}, []
        for char in s:
            if char not in pars:
                stack.append(char)
            else:
                if stack and stack[-1] == pars[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
