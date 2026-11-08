from bisect import bisect_left
class MyHashMap:

    def __init__(self):
        self.map=[]
        

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.map.append((key, value))
        self.map.sort()
        

    def get(self, key: int) -> int:
        index=bisect.bisect_left(self.map, (key,))

        if index>len(self.map)-1:
            return -1
        if self.map[index][0]!=key:
            return -1
      
        return self.map[index][1]
        

    def remove(self, key: int) -> None:
        index=bisect.bisect_left(self.map, (key,))
        if index>len(self.map)-1:
            return 
        if self.map[index][0]!=key:
            return -1
        del self.map[index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)