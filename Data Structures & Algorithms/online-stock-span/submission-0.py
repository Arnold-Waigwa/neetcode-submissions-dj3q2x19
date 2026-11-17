class StockSpanner:
    """
    [100, 80, 60, 70, 60, 75]
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            _, curr_span = self.stack.pop()
            span += curr_span
        self.stack.append((price, span))
        return span

                
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)