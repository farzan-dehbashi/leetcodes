class MovingAverage:

    def __init__(self, size: int):
        self.s = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        left = 0
        if len(self.q) > self.s:
            left = self.q.popleft()
        self.sum = self.sum + val - left
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)