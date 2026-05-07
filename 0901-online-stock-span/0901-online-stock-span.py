class StockSpanner:

    def __init__(self):
        self.stack = [] # pair store (price, span)
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:# decrease in stack maintain 
            span += self.stack[-1][1] # answer stack top se mil rha hai  and current se nahi since it is a "previous" problem
            self.stack.pop()
        self.stack.append([price,span])
        return span


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)