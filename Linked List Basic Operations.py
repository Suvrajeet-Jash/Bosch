class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # Data found and deleted
            previous = current
            current = current.next
        return False  # Data not found

    def display(self):
        current = self.head
        elems = []
        while current:
            elems.append(str(current.data))
            current = current.next
        print(" -> ".join(elems) if elems else "List is empty")

def main():
    ll = SinglyLinkedList()

    while True:
        print("\nChoose operation: append, prepend, delete, display, exit")
        choice = input("Enter choice: ").strip().lower()

        if choice == 'append':
            data = input("Enter data to append: ")
            ll.append(data)
        elif choice == 'prepend':
            data = input("Enter data to prepend: ")
            ll.prepend(data)
        elif choice == 'delete':
            data = input("Enter data to delete: ")
            if ll.delete(data):
                print(f"{data} deleted.")
            else:
                print(f"{data} not found in list.")
        elif choice == 'display':
            ll.display()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
