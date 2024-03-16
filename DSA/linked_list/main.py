class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
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

            
            
            
                
            

        


