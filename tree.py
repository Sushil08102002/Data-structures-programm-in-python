# we treat a node as a seperate object and use various methods to form a tree
class BST:
    # create a node with the BST
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    
    def insert(self,value):
        #check if tree is empty then only this node is added
        if self.data is None:
            self.data=value 
            return
        if self.data==value:      #duplicate  values are not allowed
            return
        if self.data>value:
            #value is less then the key value and can be added in left side
            '''now in this case we have two schenerios
            1) left value is null
            2) we have some node at left side'''
            if self.lchild:
                self.lchild.insert(value)
            else:
                self.lchild=BST(value)
        else:
            #value is more then the key value and can be added in right side
            '''now in this case we have two schenerios
            1) right value is null
            2) we have some node at right side'''
            if self.rchild:
                self.rchild.insert(value)
            else:
                self.rchild=BST(value)
                
    def search(self,input):
        if input==self.data:
            print("node present")
            return
        elif input<self.data:
            if self.lchild==None:
                print("NODE NOT PRESENT")
                return
            else:
                self.lchild.search(input)
        else:
            if self.rchild:
                self.rchild.search(input)
            else:
                print("Node not present")
                return
            
    def preorder(self):
        '''method used for pre-order traversal of a tree'''
        print(self.data)
        if self.lchild:
            self.lchild.preorder() 
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        '''used for in-order traversal of a tree'''
        #in-order traversal-----> left -- root -- right
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
                #print(self.rchild.data)
        print(self.data)
        
    def delete(self,value):
        # see explanation ----> https://www.youtube.com/watch?v=kDbqMBgVr9s&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=48&ab_channel=Amulya%27sAcademy
        if self.data==None:
            print("tree is empty")
            return
        '''deletion of a node take various steps but first we want the node that value which we want to delete'''
        if value<self.data:                                          # if our value present in left subtree
            if self.lchild:
                self.lchild=self.lchild.delete(value)
            else:
                print("given node is not present")
                return
        elif value>self.data:                                          #value present in right subtree
            if self.rchild:
                self.rchild=self.rchild.delete(value)
            else:
                print("Given node is not present")
                return
        else:
            '''in this case our self is equal to the node we want so now we have to
            delete that node and for this we have 3 conditiond
            1) if node has no child
            2) if node has one child
            3) if node has two child'''
            
            if self.lchild==None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild==None:
                temp=self.lchild
                self=None
                return temp
            
            '''now is we have two nodes then we can use any of the one way i.e.
            1)replace node with minimum value of right subtree
            2) replace node with maximum value of left subtree
            here we use 1st approach'''
            
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(node.data)
        return self
    
    def min_key(self):
        '''this method return minimum value of a BST'''
        current=self  # here current pointing towrds the root node
        while current.lchild:
            current=current.lchild
        print("node with minimum key is :",current.data)
        
    def max_key(self):
        '''this method return maximum value of a BST'''
        current=self
        while current.rchild:
            current=current.rchild
        print("maximum key of tree is :", current.data)
        
    
                
            
                        
def count(node):
    if node==None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)   
root=BST(None)
l=[100,50,60,20,20,30,200,150,300]
for i in l:
    root.insert(i)
# root.search(55)
# root.inorder()
if count(root)>1:                                                #this case include when we have single node in a tree
    root.delete(100)
else:
    print("node not deleted due to only one node is present")

# root.inorder()
root.min_key()
root.max_key()