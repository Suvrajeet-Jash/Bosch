class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)
    
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, current, result):
        if current:
            result.append(current.value)
            self._preorder(current.left, result)
            self._preorder(current.right, result)
    
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, current, result):
        if current:
            self._postorder(current.left, result)
            self._postorder(current.right, result)
            result.append(current.value)

# Example usage with input
if __name__ == "__main__":
    bst = BST()
    print("Enter numbers to insert into the BST (space-separated):")
    values = list(map(int, input().split()))
    for val in values:
        bst.insert(val)
    
    print("Inorder traversal (sorted):", bst.inorder())
    print("Preorder traversal:", bst.preorder())
    print("Postorder traversal:", bst.postorder())
    
    print("Enter a value to search in BST:")
    search_val = int(input())
    found = bst.search(search_val)
    print(f"Value {search_val} {'found' if found else 'not found'} in the BST.")
