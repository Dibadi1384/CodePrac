class RecentCounter:

    def __init__(self):
        self.recentreqs=[]
        

    def ping(self, t: int) -> int:
        heapq.heappush(self.recentreqs, (t))
            
        totalreqs=0

        while self.recentreqs[0]<t-3000:
            heapq.heappop(self.recentreqs)
        
        
        return len(self.recentreqs)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)