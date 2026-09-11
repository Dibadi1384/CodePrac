class RecentCounter:

    def __init__(self):
        self.counter=deque()

    def ping(self, t: int) -> int:
        #times arrive in order
        self.counter.append(t)

        #we want the from t to t-3000
        #so we go from the left to right and delete anything that is less than t-3000(smaller numbs)
        #what remains now is the from t-3000 up to t
        while self.counter[0] < t-3000:
            self.counter.popleft()
        return len(self.counter)
        # queue cannot hold more than 3000 items at each time, so since the while loops is bounded by a fixed constant the run time is O(1)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)