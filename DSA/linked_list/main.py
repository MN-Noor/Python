from linkedList import Node
from linkedList import LinkedList
LinkedList=LinkedList()
def Menu():
    status=True
   
    while True:
        print("1:IsEmpty\n2:Insert At End\n3:Display\n4:insertAt Start\n5:count nodes\n6:display even values\n7:Sum of values\n8:Find\n9:Find Minimum \n10:Delete First node\11:Exit")
        choice=int(input("Enter Choice"))
        if choice==1:
            if LinkedList.IsEmpty():
                print("List is Empty")
            else:
                print("list id not empty")

        elif  choice==2:
            data=int(input("Enter data"))
            LinkedList.insertAtEnd(data)
        elif  choice==3:
            LinkedList.display()
        elif choice==4:
            data=int(input("Enter data"))
            LinkedList.insertAtStart(data)
        elif choice==5:
            print(LinkedList.countnodes())
        elif choice==6:
            LinkedList.displayEven()
        elif choice==7:
            LinkedList.sumOfValues()
        elif choice==8:
            data=int(input("Enter data"))
            if LinkedList.find(data):
                print("element found")
            else:
                print("element  not found")

        elif  choice==9:
            min=LinkedList.FindMin()
            print(f'Min:{min}')
        elif choice==10:
            status=LinkedList.deleteFirstNode()
            if status:
                print("node Deleted")

        elif choice==11:
            head=LinkedList.reverseLinkedlist()
            print(f'head={head}')
        elif choice==12:
            status=False
            break
    
if __name__=="__main__":
    Menu()


    


            

        


