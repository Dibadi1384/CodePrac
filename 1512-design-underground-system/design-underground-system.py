class UndergroundSystem:

    def __init__(self):
        
        self.customers=defaultdict(list)
        self.times=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id]=[stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,start=self.customers[id][0],self.customers[id][1]
        path=startStation+"."+stationName
        totaltime=abs(t-start)

        if path in self.times:
            self.times[startStation+"."+stationName].append(totaltime)
        else:
            self.times[startStation+"."+stationName]=[totaltime]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path=startStation+"."+endStation
        summ=0
        if path in self.times:
            for time in self.times[path]:
                summ+=time
        return summ/len(self.times[path])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)