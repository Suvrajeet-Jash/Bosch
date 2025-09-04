class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


def main():
    stack = Stack()
    
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Size")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
            print(f"'{item}' pushed to stack.")
        
        elif choice == '2':
            popped = stack.pop()
            if popped is None:
                print("Stack is empty, cannot pop.")
            else:
                print(f"Popped item: {popped}")
        
        elif choice == '3':
            top = stack.peek()
            if top is None:
                print("Stack is empty.")
            else:
                print(f"Top item: {top}")
        
        elif choice == '4':
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        
        elif choice == '5':
            print(f"Stack size: {stack.size()}")
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
