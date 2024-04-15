class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        while temp!=None:
            print(f'{temp.value}-->')
            temp=temp.next
    def displayReverse(self):
        temp=self.tail
        while temp!=None:
            print(f"{temp.value}-->")
            temp=temp.prev
    def isEmpty(self):
        if self.head==None:return True
    def insertAtStart(self,value):
        newnode=Node(value)
        if self.isEmpty():
            head=newnode
            prev=newnode
            return
        else:
            newnode.next=head
            head.prev=newnode
            head=newnode

    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.isEmpty():
            head=newNode
            prev=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    def insertBefore(self,index,value):
        newNode=Node(value)
        if self.isEmpty():head=tail=value
        if self.head.value==index:
            self.insertAtStart(value)
        elif self.tail.value==index:
            self.insertAtEnd
        else:
            temp=









    