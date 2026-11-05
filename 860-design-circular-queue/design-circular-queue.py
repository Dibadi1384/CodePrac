class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head=ListNode(0,None,None)
     
        self.tail=ListNode(0,None,None)
        self.head.next=self.tail
        self.head.prev=None
        self.tail.next=None
        self.tail.prev=self.head

        self.size=0
        self.cap=k

    def enQueue(self, value: int) -> bool:
        if (self.cap==self.size):
            return False
        
        else:
            self.size+=1
            newnode=ListNode(value,None,None)

            self.tail.prev.next=newnode
            newnode.prev=self.tail.prev
            newnode.next=self.tail
            self.tail.prev=newnode
            
        return True


        

    def deQueue(self) -> bool:
        if self.size==0:
            return False
        self.size-=1
        
  
        self.head.next=self.head.next.next
        self.head.next.prev=self.head
        
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val


    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size==self.cap:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()