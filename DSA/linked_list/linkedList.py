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
        if self.IsEmpty():
            self.head=node
        else:
            cur_node=self.head
            while  cur_node.next!=None:
                cur_node=cur_node.next
            cur_node.next=node

    def countnodes(self):
        count=0
        if  self.IsEmpty():
            return 0
        else:
            current=self.head
            while  current!=None:
                current=current.next
                count+=1
            return count
    def display(self):
        if  self.IsEmpty():
            print("linked list is  empty")
        else:
            curr=self.head
            while curr!=None:
                print(f'{curr.data} ,', end="")
                curr=curr.next


    def displayEven(self):
        if self.IsEmpty():
            print("Linked  list is Empty")
        else:
            current=self.head
            while current!=None:
                if current.data %2==0:
                    print(current.data)
                current=current.next

    def sumOfValues(self):
        if self.IsEmpty():
            return 0
        else:
            sum=0
            current=self.head
            while current!=None:
                sum+=current.data
                current=current.next
            return sum
        
    def find(self,value):
        if self.IsEmpty():
            return False
        else:
            current=self.head
            while current!=None:
                if current.data==value:
                    return True
                current=current.next
            return False
    def deleteFirstNode(self):
        if self.IsEmpty():
            print("linkedList is Empty")
            return False
        else:
            self.head=self.head.next
            return True
        
    def  FindMin(self):
        if self.IsEmpty():
            return -1
         
        curr=self.head
        mi=curr.data
        while curr.next!=None:
            curr=curr.next
            mi=min(mi,curr.data)
        return mi
    def deleteValue(self,value):
        temp=self.head
        while temp!=None and temp.data!=value:
            prev=temp
            temp=temp.next

    def reverseLinkedlist(self):
        if self.IsEmpty():
            return -1
        prev,curr=None,self.head
        while curr!=None:
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1
        self.head=prev
        return self.head


    







            
            