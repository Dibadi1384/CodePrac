class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sorting is n
        trips.sort(key=lambda x: x[1])

        rides=[]
        passangers=0

        for trip in trips:
            while rides and rides[0][0]<=trip[1]:
                #log n pop from the heap and o log on for the push
                end,leavingpassengers=heappop(rides)
                passangers-=leavingpassengers
            if passangers+trip[0]>capacity:
                return False
            
            passangers+=trip[0]
            heapq.heappush(rides, (trip[2],trip[0]))
        return True