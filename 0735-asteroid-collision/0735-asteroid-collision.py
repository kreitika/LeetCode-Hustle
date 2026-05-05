class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < -i:
                    stack.pop()
                    continue # stack top burst ho gaya abh new stack[-1] ke saath check kro
                elif stack[-1] == -i:
                    stack.pop()
                break #naya asteroid laao i got bursted
            else: #matlab agar stack empty hai or the direction of stack top and i are in opposite directions or same directions
                stack.append(i)
        return stack
        