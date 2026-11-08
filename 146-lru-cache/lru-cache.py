class ListNode():
    def __init__(self, next: ListNode(), prev: ListNode(), val: int, key: int):
        self.next=next
        self.prev=prev
        self.key=key
        self.val=val

class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.cache={}
        self.head=ListNode(None, None, 0, 0)
        self.tail=ListNode(None, None, 0, 0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def remove(self, node: ListNode())->None:
        node.prev.next = node.next
        node.next.prev = node.prev    

    def add(self, node: ListNode())->None:
        prenode=self.tail.prev
        prenode.next=node

        node.prev=prenode
        node.next=self.tail
        self.tail.prev=node



    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])   
            return self.cache[key].val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size==self.cap:
                nodetoremove=self.head.next
                del self.cache[nodetoremove.key]
                self.remove(nodetoremove)
                self.size-=1
                

            self.size+=1
            self.cache[key]=ListNode(None, None, value, key)
            self.add(self.cache[key])
        else:
            self.cache[key].val=value
            self.remove(self.cache[key])
            self.add(self.cache[key])

   
    
    
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)