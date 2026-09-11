class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[1])

        rides=[]
        passangers=0

        for trip in trips:
            while rides and rides[0][0]<=trip[1]:
                end,leavingpassengers=heappop(rides)
                passangers-=leavingpassengers
            if passangers+trip[0]>capacity:
                return False
            
            passangers+=trip[0]
            heapq.heappush(rides, (trip[2],trip[0]))
        return True