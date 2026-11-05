class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize=maxSize
        self.stack=deque()
        

    def push(self, x: int) -> None:
        
        if len(self.stack)<self.maxsize:
            self.stack.append(x)
        print(self.stack)
        
        

    def pop(self) -> int:
        
        if not self.stack:
            return -1
        return self.stack.pop()
        
        

    def increment(self, k: int, val: int) -> None:
        limit=0
        if k>len(self.stack):
            limit=len(self.stack)
        else:
            limit=k
        for i in range(limit):
            self.stack[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)