class Queue:
    def __init__(self) -> None:
        self.items=[]*5
        self.front=0
        self.rear=0
        
    #To perform Enque operation on Queue
    def enque(self,item):
        self.items.append(item)
        self.rear+=1
        
        
    # TO perform Deque operaation on Queue
    def deque(self):
        if self.front==self.rear==0:
            print("Empty Queue!")
        elif self.front==self.rear!=0:
            #condition of single element
            self.front=self.rear=0
            print("Empty Queue!")
        else:
            self.items.pop(0)
            self.front+=1
            
    def isFull(self):
        if self.rear==len(self.items)-1:
            print("True")
        else:
            print("False")      
    
    def isEmpty(self):
        if self.rear==0:
            print("True")
        else:
            print("False")
                  
            
s=Queue()          
s.enque(5) 
s.isEmpty()
