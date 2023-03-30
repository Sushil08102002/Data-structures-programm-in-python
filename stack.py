class Stack:
    
    def __init__(self) -> None:
        self.items=[]
        
    def push(self,item) -> None:
        self.items.append(item)
        
    def  pop(self) -> None:
        if not self.items:
            pass
        else:
            self.items.pop()
    
    def peek(self):
        if not self.items:
            return None
        else:
            return self.items[len(self.items)-1]    
    
    def isEmpty(self):
        if not self.items:
            print("True")        
        else:
            print("False")
        
s=Stack()
s.push(5)        
s.push(10)
s.push(20)
print(s.items)
print(s.peek())
s.isEmpty()
print(s.items)
s.pop()
s.pop()
s.pop()
s.isEmpty()
