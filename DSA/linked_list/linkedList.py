class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def IsEmpty(self):
        if self.head==None:return True
    def  insertAtStart(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def insertAtIndex(self,data,pos):
        cur_pos=1
        new_node=Node(data)
        curr_node=self.head
        if cur_pos==pos:
            self.head=new_node
        else:
            while curr_node.next!=None  and cur_pos+1==pos:
                curr_node=curr_node.next
                cur_pos+=1
            new_node.next=curr_node
            curr_node.next=new_node
    def insertAtEnd(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
        else:
            cur_node=self.head
            while  cur_node.next!=None:
                cur_node=cur_node.next()
            cur_node.next=node
    def countnodes(self):
        count=0
        if  self.isEmpty():
            return 0
        else:
            while(current.next!=None):
                current=self.head
                current=current.next
                count+=1
            return count
    def display(self):

        if  self.IsEmpty():
            print("linked list is  empty")
        else:
            curr=self.head
            while curr.next!=None:
                print(curr.data)
                curr=curr.next



    def displayEven(self):
        if self.IsEmpty():
            print("Linked  list is Empty")
        else:
            current=self.head
            while current.next!=None:
                if current.data %2==0:
                    print(current.data)
                    current=current.next
    def sumOfValues(self):
        if self.isEmpty():
            return 0
        else:
            sum=0
            current=self.head
            while current.next!=None:
                sum+=current.data
                current=current.next
            return sum
        
    def find(self,value):
        if self.IsEmpty():
            return False
        else:
            current=self.head
            while current.next!=None:
                if current.data==value:
                    return True
                current=current.next
            return False
    def deleteFirstNode(self):
        if self.IsEmpty():
            print("linkedList is Empty")
        else:
            self.head=self.head.next
    def  FindMin(self):
        if self.IsEmpty():
            return -1
            
        curr=self.head
        ma=curr
        while curr.next!=None:
            curr=curr.next
            ma=max(ma,curr)
        return ma
        
    







            
            