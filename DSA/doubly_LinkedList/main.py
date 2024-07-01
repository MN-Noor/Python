from doublyList import LinkedList
def main():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Display List")
        print("2. Display List in Reverse")
        print("3. Insert at Start")
        print("4. Insert at End")
        print("5. Insert Before")
        print("6. Insert After")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            linked_list.display()
        elif choice == 2:
            linked_list.displayReverse()
        elif choice == 3:
            value = int(input("Enter value to insert at start: "))
            linked_list.insertAtStart(value)
        elif choice == 4:
            value = int(input("Enter value to insert at end: "))
            linked_list.insertAtEnd(value)
        elif choice == 5:
            value = int(input("Enter index value to insert before: "))
            index = int(input("Enter new value to insert: "))
            found=linked_list.insertBefore(value, index)
            if found ==False:
                print("value not found")
            else:
                print("value not found")
        elif choice == 6:
            value = int(input("Enter index value to insert after: "))
            index = int(input("Enter new value to insert: "))
            found=linked_list.insertAfter(value, index)
            if found==False:
                print("Value not found")
            else:
                print("value found")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()