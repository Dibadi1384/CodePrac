class SnapshotArray:

    def __init__(self, length: int):
        self.array=[0]*length
        self.snapID=-1
        self.snapshots=[[(-1,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.array[index]=val
        if self.snapshots[index] and self.snapshots[index][-1][1]!=val:
            self.snapshots[index].append((self.snapID,val))
        else:
            self.snapshots[index].append((self.snapID,val))
     
        
    def snap(self) -> int:
        self.snapID+=1
        return self.snapID

    def get(self, index: int, snap_id: int) -> int:
        indexhistory=self.snapshots[index]
        i=bisect.bisect_left(indexhistory, (snap_id,))-1
        i=min(i, len(indexhistory)-1)
        return indexhistory[i][1]


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)