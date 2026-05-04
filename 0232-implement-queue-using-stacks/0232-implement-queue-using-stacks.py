class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        # if s2 is empty transfer elements from s1 
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        #return top most element from s2 (whether it is empty or not, if its empty forst fill it with s1 above)
        return self.s2.pop()
        

    def peek(self) -> int:
        # if s2 is empty transfer elements from s1 
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        #return top most element from s2 (whether it is empty or not, if its empty forst fill it with s1 above)
        return self.s2[-1]
        

    def empty(self) -> bool:
        #we need to check if both stacks s1 and s2 are empty, since len cant be negative we can check the max of len(s1,s2) == 0 if true then both are empty
        return max(len(self.s1), len(self.s2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()