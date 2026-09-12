class MovingAverage:

    def __init__(self, size: int):
        self.sum=0
        self.nums=deque()
        self.size=size

    def next(self, val: int) -> float:
        if len(self.nums)==self.size:
            self.sum-=self.nums.popleft()
        self.sum+=val
        self.nums.append(val)
         
        
        return self.sum/(len(self.nums))

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)