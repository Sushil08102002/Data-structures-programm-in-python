class PriorityQueue:
    def __init__(self):
        self.items={}
        self.front=0
        self.rear=0
        
    def enque(self,item,priority):
        self.items[priority]=item
        self.rear+=1
        
    def deque(self):
        if self.front==self.rear==0:
            print("!Empty Queue")
        elif self.front==self.rear!=0:
            print("Empty queue")
            self.front=self.rear=0
        else:
            prior=min(self.items.keys())
            self.items.pop(prior)
            self.front+=1
        
    
s=PriorityQueue()
s.enque(2,1)
s.enque(5,1)
s.enque(10,2)
s.deque()
print(s.items)
