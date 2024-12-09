'''creating a single node i.e Node======> |data | null | ----> this is single node'''
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class Linked_list:
    def __init__(self) -> None:
        self.head=None   # linked list is empty initially 
    
    
    def add_begin(self,data):
        '''used to add node at beggning of linked list'''
        node=Node(data)
        node.ref=self.head
        self.head=node
    
    #count is used to check how many elements present in a linked list
    def count(self):
        if self.head==None:
            return 0
        else:
            n=self.head
            count=0
            while n is not None:
                n=n.ref
                count+=1
            print(f"\n{count}")
        
    def add_end(self,data):
        '''used to add node at end of the linked list'''
        node=Node(data)
        if self.head==None:
            self.head=node
        else:    
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=node
        
        
    def traversal(self):
        '''used to print linked list'''
        n=self.head                              
        if n is None:
            print("Linked List is empty")
        else:
            while(n!=None):
                print(n.data,end=" -> ")
                n=n.ref                         
        
    def add_after(self,data,prev_data):
        '''add node after a value '''
        n=self.head
        while n!=None:
            if n.data==prev_data:
                break
            n=n.ref
        if n==None:
            print("Value not found")
        elif n.data==prev_data:
            node=Node(data)
            node.ref=n.ref
            n.ref=node

    def add_before(self,data,next_elem):
        '''used to add node before a given element'''
        if self.head==None:
            print("Empty linked list ")
            return
        elif self.head.data==next_elem:
            #if we found element at first position of linked list
            node=Node(data)
            node.ref=self.head
            self.head=node
        else:
            #if we want to add element in between then we want to know previous node of given node
            n=self.head
            while n.ref!=None:
                if n.ref.data==next_elem:
                    break
                else:
                    n=n.ref
            if n.ref==None:
                print("element not found")
                return
            else:
                node=Node(data)
                node.ref=n.ref
                n.ref=node
                return
            
    def remove_begin(self):
        '''remove node from beggning'''
        if self.head==None:
            print("empty linked list")
            return
        elif self.head.ref==None:
            self.head=None
            return
        else:
            self.head=self.head.ref
            return
        
    def remove_end(self):
        '''remove node from the end of linked list'''
        if self.head==None:
            print("Empty Linked-List")
            return
        elif self.head.ref==None:
            self.head=None
            return
        else:
            n=self.head
            while(n.ref.ref!=None):
                n=n.ref
            n.ref=None
            
    def remove_by_value(self,x):
        '''remove the node by its value'''
        if self.head==None:
            print("Empty Linked List")
            return
        if x==self.head.data:
            self.head=self.head.ref
        else:
            n=self.head
            while (n.ref.data!=x):
                n=n.ref
            n.ref=n.ref.ref 
                
                    
if __name__=="__main__":
    l=Linked_list()
    l.add_begin(10)
    l.add_end(20)
    l.add_end(30)
    l.add_end(40)
    l.add_end(50)
    l.traversal() 
    l.count()