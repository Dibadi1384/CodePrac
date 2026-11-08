class Allocator:

    def __init__(self, n: int):
        self.n=n
        self.free=[]
        self.mem={}
        heapq.heappush(self.free, (0,n))
        

    def allocate(self, size: int, mID: int) -> int:
        if not self.free:
            return -1

        
        # First merge adjacent free intervals
        merged = []

        while self.free:
            start, end = heapq.heappop(self.free)

            if merged and merged[-1][1] >= start:
                merged[-1] = (
                    merged[-1][0],
                    max(merged[-1][1], end)
                )
            else:
                merged.append((start, end))

        self.free = merged
        heapq.heapify(self.free)
        start,end=heapq.heappop(self.free)

        tempheap=[]

        while (end-start)<size and self.free:
            heapq.heappush(tempheap, (start,end))
            start,end=heapq.heappop(self.free)

        self.free+=tempheap
        heapq.heapify(self.free)
        
        if end-start<size or start+size>self.n:
            heapq.heappush(self.free, (start,end))
            return -1
        
        if end-start>size:
            heapq.heappush(self.free, (start+size,end))
        
        if mID not in self.mem:
            self.mem[mID]=[]
        self.mem[mID].append((start, start+size))

  

        return start

    def freeMemory(self, mID: int) -> int:
        if mID in self.mem:
            res=0
            for block in self.mem[mID]:
                res+=(block[1]-block[0])
                heapq.heappush(self.free, (block[0], block[1]))
            del self.mem[mID]
            return res
        return 0
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)