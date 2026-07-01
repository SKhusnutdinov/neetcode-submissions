class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        newDays = 1
        while self.st and price >= self.st[-1][0]:
            oldPrice, oldDays = self.st.pop()
            newDays += oldDays
        self.st.append((price, newDays))
        return newDays


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)