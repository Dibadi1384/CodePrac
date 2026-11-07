from sortedcontainers import sorteddict
from bisect import bisect_left, bisect_right

class TimeMap:
    def __init__(self):
        self.keys={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key]=SortedDict()

        self.keys[key][timestamp]= value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        index=self.keys[key].bisect_right(timestamp)-1
        if index<0:
            return ""
        return self.keys[key].peekitem(index)[1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)