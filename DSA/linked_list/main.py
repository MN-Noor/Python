from linkedList import Node
from linkedList import LinkedList
LinkedList=LinkedList()
def Menu():
    status=True
   
    while True:
        print("1:IsEmpty\n2:Insert At End\n3:Display\n4:insertAt Start\n5:count nodes\n6:display even values\n7:Sum of values\n8:Find\n9:Find Minimum \n10:Delete First node\n11:Destructer\n12:Exit")
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
            data=input("Enter data")
            LinkedList.insertAtStart(data)
        elif choice==5:
            LinkedList.countnodes()
        elif choice==6:
            LinkedList.displayEven()
        elif choice==7:
            LinkedList.sumOfValues()
        elif choice==8:
            if LinkedList.find():
                print("element found")
            else:
                print("element  not found")
        elif  choice==9:
            min=LinkedList.FindMin()
            print("Min:"+min)
        elif choice==10:
            status=LinkedList.deleteFirstNode()
            if status:
                print("node Deleted")

        # elif choice==11:
        elif choice==12:
            status=False
    
if __name__=="__main__":
    Menu()


    


            

        


