class MyCircularDeque:

    def __init__(self, k: int):
        self.dq=collections.deque([None]*k)
        self.k=k
        self.p1=0
        self.p2=1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.dq[self.p1]=value
            self.p1=(self.p1-1)%self.k
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.dq[self.p2]=value
            self.p2=(self.p2+1)%self.k
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dq[(self.p1+1)%self.k]=None
            self.p1=(self.p1+1)%self.k
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dq[(self.p2-1)%self.k]=None
            self.p2=(self.p2-1)%self.k
            return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dq[(self.p1+1)%self.k]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dq[(self.p2-1)%self.k]
        

    def isEmpty(self) -> bool:
        if (self.p1+1)%self.k==self.p2 and self.dq[self.p1] is None:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if (self.p1+1)%self.k==self.p2 and self.dq[self.p1] is not None:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()