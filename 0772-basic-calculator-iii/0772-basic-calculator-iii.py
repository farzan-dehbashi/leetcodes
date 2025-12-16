class Solution:
    def calculate(self, s: str) -> int:
        def calc(i):
            stack = []
            num = 0
            op = '+'  # operator before current number
            
            while i < len(s):
                ch = s[i]
                
                # Build number from digits
                if ch.isdigit():
                    num = num * 10 + int(ch)
                
                # When we see '(', recursively solve what's inside
                if ch == '(':
                    num, i = calc(i + 1)  # get result and new position
                
                # When we see operator, ')', or reach end: apply the operator
                if ch in '+-*/)' or i == len(s) - 1:
                    # Apply the operator we saved
                    if op == '+':
                        stack.append(num)
                    if op == '-':
                        stack.append(-num)
                    if op == '*':
                        stack.append(stack.pop() * num)
                    if op == '/':
                        stack.append(int(stack.pop() / num))
                    
                    # If we hit ')', we're done with this sub-expression
                    if ch == ')':
                        return sum(stack), i
                    
                    # Save this operator for next number
                    op = ch
                    num = 0
                
                i += 1
            
            return sum(stack), i
        
        return calc(0)[0]  # return just the result, not position