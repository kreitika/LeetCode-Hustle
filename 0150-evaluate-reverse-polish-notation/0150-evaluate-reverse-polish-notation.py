class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                den = stack.pop()
                num = stack.pop()
                stack.append(int(num/den))
            elif i == '-':
                sec = stack.pop() 
                first = stack.pop()
                stack.append(first - sec)
            else:
                stack.append(int(i))
        return stack[-1]
        