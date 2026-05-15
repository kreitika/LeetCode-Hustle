class FreqStack:

    def __init__(self):
        self.cnt = {} # hashmap har no. ki frequency ke liye
        self.maxCnt = 0 # maximum freq at any point of time in total
        self.stacks = {} # har frequency ke corresponding stack 
        

    def push(self, val: int) -> None:
        temp = 1 + self.cnt.get(val, 0)
        self.cnt[val] = temp
        if temp > self.maxCnt:
            self.maxCnt = temp
            self.stacks[temp] = []
        self.stacks[temp].append(val) 
        

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()