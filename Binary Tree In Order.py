class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def inorder(root):
    if root:
        inorder(root.left)         # 1. Traverse left
        print(root.key, end=" ")   # 2. Visit root
        inorder(root.right)        # 3. Traverse right
 
# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
 
print("Inorder Traversal:")
inorder(root)
