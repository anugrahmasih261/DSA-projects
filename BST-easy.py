class BSTNode:
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.left = None  # Initialize the left child to None
        self.right = None  # Initialize the right child to None

    # Method to insert a new node in the BST
    def insert(self, data):
        if data < self.data:  # If the data is smaller, go to the left
            if self.left is None:  # If no left child, create one
                self.left = BSTNode(data)
            else:
                self.left.insert(data)  # Recursively insert in the left subtree
        else:  # If the data is larger, go to the right
            if self.right is None:  # If no right child, create one
                self.right = BSTNode(data)
            else:
                self.right.insert(data)  # Recursively insert in the right subtree

    # Method to search for a value in the BST
    def search(self, data):
        if data == self.data:  # If the data matches the current node, found it
            return True
        elif data < self.data and self.left:  # If smaller, search in the left subtree
            return self.left.search(data)
        elif data > self.data and self.right:  # If larger, search in the right subtree
            return self.right.search(data)
        else:
            return False  # If not found in any subtree

# Create a BST and insert some elements
root = BSTNode(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

# Search for elements in the BST
print("Is 40 in the BST?", root.search(40))  # Output: True
print("Is 25 in the BST?", root.search(25))  # Output: False
