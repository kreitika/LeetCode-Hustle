class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{': stack.append(c)
            if c == ')':
                if stack :
                   val = stack.pop()
                   if val != '(': return False
                else: return False
            if c == ']':
                if stack :
                   val = stack.pop()
                   if val != '[': return False
                else: return False
            if c == '}':
                if stack :
                   val = stack.pop()
                   if val != '{': return False
                else: return False
        if stack : return False
        else: return True


        