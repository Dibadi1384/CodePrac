class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.stream=nums
        self.stream.sort()
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        klargest=len(self.stream)-self.k
        return self.stream[klargest]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)