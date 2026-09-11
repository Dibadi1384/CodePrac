from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=SortedDict()
        #Inserting into SortedDict is o(logn)
        self.timemap[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        #bisect is binary search is its O(logn) cuz we cut the search space in half each time
        if key not in self.timemap or self.timemap[key].bisect_right(timestamp)==0:
            return ""

        return (self.timemap[key].peekitem( self.timemap[key].bisect_right(timestamp)-1)[1])

        
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)