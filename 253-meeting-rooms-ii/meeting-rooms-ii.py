class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not  intervals:
            return 0

        free_rooms=[]

        intervals.sort(key= lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            #if the start time is bigger than the ending time of the latest ending
            if free_rooms[0]<=i[0]:
                heapq.heappop(free_rooms) #free that room

            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

            
         


