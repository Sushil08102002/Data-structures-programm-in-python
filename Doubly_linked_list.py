class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pref=None
        self.nref=None



class doublyLL:
    def __init__(self) :
        self.head=None
        
#******************************************* Traversing of LL starts***************************************        
    def print_forward(self):
        n=self.head
        if n is None:                                          #firstly check our linked list is empty or not
            print("Linked List is Empty!")
        else:
            while(n!=None):
                print(n.data,end="->")
                n=n.nref
    
    def print_reverse(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            n=self.head
            while(n.nref!=None):
                n=n.nref
            while(n!=None):
                print(n.data,end="->")
                n=n.pref
#************************************************************************************************************               
                
#***************************************insertion operation of DLL ends**************************************               
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is not Empty!!")
            
    def insert_begin(self,data):
        if self.head is None:
            self.insert_empty(data)
        else:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
            
    def insert_end(self,data):
        if self.head is None:
            self.insert_empty(data)
        else:
            n=self.head
            while(n.nref!=None):
                n=n.nref
            new_node=Node(data)
            new_node.pref=n
            n.nref=new_node
            
    def insert_before(self,x,data):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref                
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node   # this line is added to shift our head from previous node to newnode
                n.pref = new_node
    
    def insert_after(self,x,data):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("value not present in Linked List!")
            else:
                new_node=Node(data)    #creating a node
                #here 2 condition occur weather node add after last node or at rest of the positions
                if n.nref==None:   # we found our value at lastnode
                    n.nref=new_node
                    new_node.pref=n
                #we insert our node at rest of the positions
                else:
                    new_node.pref=n
                    new_node.nref=n.nref
                    n.nref.pref=new_node
                    n.nref=new_node
#************************************************************************************************************


#************************Deletion Operations on list ******************************************************
    
    def remove_begin(self):
        if self.head==None:
            print("Empty Linked List!!")
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            self.head=self.head.nref
            self.head.pref=None
            
    def remove_end(self):
        if self.head==None:
            print("Empty Linked List!!")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            if n.pref==None:      # check if we are removing first node so condition is different
                self.head=None
            else:
                n.pref.nref=None
                
    def remove_by_value(self,x):
        '''we apply  conditions i.e.
        1)linked list is empty
        2) only one node present in ll
        3) delete first node 
        4) delete last node
        5) delete middle node'''
        n=self.head
        if self.head==None:
            print("linked list is empty")
        elif self.head.nref==None:
            #only one node present
            self.head=None
        else:
            while n.nref!=None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            if n.nref==None and n.data!=x:  #if we reached to last node and value not found
                print("node not present in linked list")
            else:
                if n.pref==None:           # we delete first node
                    self.remove_begin()
                elif n.nref==None:         #we delete last node
                    self.remove_end()
                else:                      #we delete middle nodes
                    n.pref.nref=n.nref
                    n.nref.pref=n.pref
                
        
                
                
        
        
            
                
    
                
                
if __name__=="__main__":
    dl1=doublyLL()
    dl1.insert_begin(17)
    dl1.insert_before(17,20)
    dl1.insert_after(17,25)
    dl1.insert_begin(15)
    dl1.remove_by_value(17)
    dl1.remove_by_value(15)
    dl1.remove_by_value(20)
    dl1.remove_by_value(25)
    dl1.remove_by_value(27)
    dl1.print_forward()
    
                
        