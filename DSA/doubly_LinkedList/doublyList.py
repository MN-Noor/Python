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
            print(str(temp.value)+"-->")
            temp=temp.next
    def displayReverse(self):
        temp=self.tail
        while temp!=None:
            print(str(temp.value)+"<--")
            temp=temp.prev
    def isEmpty(self):
        if self.head==None:return True
    def insertAtStart(self,value):
        newnode=Node(value)
        if self.isEmpty():
            self.head=self.tail=newnode
            return
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.prev=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode

    def insertBefore(self,value,index):
        print("hello")
        if self.isEmpty():
            print("helo")
            return False
        elif self.head.value==index:
            print("hello")
            self.insertAtStart(value)
            return True
        else:
            print("hello")
            temp=self.head.next
            while temp!=None:
                if temp.value==index:
                    print("hello")
                    newNode=Node(value)
                    newNode.prev=temp.prev
                    newNode.next=temp
                    temp.prev.next=newNode
                    temp.next=newNode
                    return True
            return False
                    

    def insertAfter(self,value,index):
        newNode=Node(value)
        if self.isEmpty:return False
        elif self.tail==index:
            self.tail.next=newNode
            newNode.prev=self.prev
            self.tail=newNode
            return True
        else:
            temp=self.head
            while self.next==None:
                if temp.value==index:
                    newNode.next=temp.next
                    newNode.prev=temp
                    temp.next=newNode
                    newNode.next.prev=newNode
                    return True
            return False




                









    