class ListNode():
    def __init__(self, value):
        self.next=None
        self.prev=None
        self.value=value

class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.cap=0
        self.head=ListNode(0)
        self.tail=ListNode(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        

    def enQueue(self, value: int) -> bool:
        #you want to add a node to the tail(before the tail)
        if self.isFull():
            return False

        node=ListNode(value)
        prevnode=self.tail.prev
        prevnode.next=node
        node.prev=prevnode
        node.next=self.tail
        self.tail.prev=node
        self.cap+=1
        return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        #you want to remove the node before head
        firstnode=self.head.next
        firstnode.next.prev=self.head
        self.head.next=firstnode.next

        self.cap-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.value
        #the node before tail
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.value
        #the node after head
        

    def isEmpty(self) -> bool:
        #if cap is 0
        if self.cap==0:
            return True
        return False

    def isFull(self) -> bool:
        #is cap is equal to size
        if self.cap==self.size:
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